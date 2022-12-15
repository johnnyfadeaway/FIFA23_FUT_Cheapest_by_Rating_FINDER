import pandas as pd
import numpy as np
import requests
import json
import requests
from datetime import datetime
from bs4 import BeautifulSoup
import re
import os

class player: # player class used data collecting from scaping
    def __init__(self, name, club, league, rating, nationality, position, price):
        self.name = name
        self.club = club
        self.league = league
        self.nationality = nationality
        self.rating = rating
        self.position = position
        self.price = price 
        

list_players = []

if os.path.exists("cache.json"): # if cache exists, load data from cache
    with open("cache.json", 'r') as openfile:
        cache_dict = json.load(openfile)

    for i in range(len(cache_dict["name"])): # use cache to fill up the player objects
        name = cache_dict["name"][i]
        club = cache_dict["club"][i]
        league = cache_dict["league"][i]
        rating = cache_dict["rating"][i]
        nationality = cache_dict["nationality"][i]
        position = cache_dict["position"][i]
        price = cache_dict["price"][i]
        list_players.append(player(name, club, league, rating, nationality, position, price))

else: # if cache does not exists, scrap data from www.futbin.com, this takes about 6 hours.
    for page_num in range(1,604):
        base_url = "https://www.futbin.com/players?page="
        header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
        response = requests.get(base_url + str(page_num), headers = header)
        if response.status_code != 200:
            print("Error occured when fetching page {}".format(page_num))
            continue
        else:
            soup1 = BeautifulSoup(response.text, "html.parser")
            players_list = soup1.find_all("tr")
            for player_idx in range(0, len(players_list), 2):
                player_url = players_list[player_idx].get("data-url")
                response2 = requests.get("https://www.futbin.com"+player_url, headers=header)
                if response2.status_code != 200:
                    print("Error occured when fetching player{} on page {}".format(player_idx,page_num))
                    continue
                soup2 = BeautifulSoup(response2.text, "html.parser")
                name = re.findall(r"^.* FIFA", str(soup2.title.string))[0][0:-5]
                club = str(players_list[player_idx].span.find_all("a")[0].get("data-original-title"))
                nationality = str(players_list[player_idx].span.find_all("a")[1].get("data-original-title"))
                league = str(players_list[player_idx].span.find_all("a")[2].get("data-original-title"))
                rating = str(players_list[player_idx].find_all("span")[1].string)
                position = str(players_list[player_idx].find_all("div")[-6].string)
                price = re.findall("^<span class=\"ps4_color font-weight-bold\">[0-9.A-Z]+", str(players_list[player_idx].find_all("span")[2]))[0][41:]
                if price == "0":
                    continue
                list_players.append(player(name, club, league, rating, nationality, position, price))
        print("Page {} done!".format(page_num))
    
    cache_dict = {} # put the players objects into a dictionary.
    cache_dict["name"] = [player.name for player in list_players]
    cache_dict["club"] = [player.club for player in list_players]
    cache_dict["league"] = [player.league for player in list_players]
    cache_dict["nationality"] = [player.nationality for player in list_players]
    cache_dict["rating"] = [player.rating for player in list_players]
    cache_dict["position"] = [player.position for player in list_players]
    cache_dict["price"] = [player.price for player in list_players]

    with open("cache.json", "w") as outfile: # save the dictionary as cahce
        json.dump(cache_dict, outfile)

def str2num(str):
    """
        input: str, e.g. "1.5M" or "1.6K"
        output: price e.g. 1500000 or 1600
    """
    num = float(re.findall("^[0-9.]+", str)[0])
    unit_list = re.findall("[MK]", str)
    if unit_list == []:
        return int(num)
    else:
        if unit_list[0] == "K":
            return int(num * 1000)
        elif unit_list[0] == "M":
            return int(num * 1000000)


for player in list_players:
    player.price = str2num(player.price)

def obj2dict(player):
    """
        input: player object
        output: turns that play object into a dictionary for creating trees later
    """ 
    player_dict = {}
    player_dict["name"] = player.name
    player_dict["club"] = player.club
    player_dict["league"] = player.league
    player_dict["rating"] = player.rating
    player_dict["nationality"] = player.nationality
    player_dict["position"] = player.position
    player_dict["price"] = player.price
    return player_dict

# creating the empty rating dictionary, each rating will be filled with a list of player's dictionarys of that rating
rating_dict = {
    "82":[],
    "83":[],
    "84":[],
    "85":[],
    "86":[],
    "87":[],
    "88":[],
    "89":[],
    "90":[],
    "91":[],
    "92":[],
}
# fill up the rating dictionary
for player in list_players:
    if player.rating in ["82", "83", "84", "85", "86", "87", "88", "89", "90", "91", "92"]:
        rating_dict[player.rating].append(obj2dict(player))
    else:
        if player.rating == "81": # we don't care about players that has ratings lower than 82, becasue they are 
                                  # too cheap and rarely used for SBCs.
            break
        else:
            continue

# sort each list in the dictionary, so that when we create the trees later, they will be balanced trees.
for i in rating_dict:
    rating_dict[i].sort(key=lambda x: x["price"])

def insert(tree, player):
    """
        note: this is a recursive function for inserting a player to the BST
        input: tree -> current tree
               player -> the player dictionary
        output: the inserted tree 
    """

    if player["price"] <= tree[0]["price"]:
        if tree[1] == []:
            tree[1] = [player,[],[]]
            return 
        else:
            insert(tree[1], player)
            return
    else:
        if tree[2] == []:
            tree[2] = [player,[],[]]
            return
        else:
            insert(tree[2], player)
            return



for i in rating_dict: # creating each tree

    root = rating_dict[i][len(rating_dict[i]) // 2]
    rating_dict[i].pop(len(rating_dict[i]) // 2)
    tree = [root, [], []]

    for player in rating_dict[i]:
        insert(tree, player)
    
    with open("{}_tree.json".format(i), "w") as outfile:
        json.dump(tree, outfile) # save each tree as a json file



