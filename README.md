# FIFA23_FUT_Cheapest_by_Rating_FINDER
F23 UMich SI507 final project

# Description
To run this program, clone the repo, if you want to scrap the latest data from www. futbin.com, then run python3 data_processing.py(please be aware that this program takes 6 hours to run) and python3 main.py sequentially. If you want to use cache, then just run python3 main.py.

# Interface
The user will first be asked to input a rating, then the program would output the k players with the lowest market values of that rating, or the k players with the highest market values of that rating, the user will also have a choice to displace the full output or the concise output.

# Data structure
After all the data is retrieved, each player’s data is turned into a dictionary. After that, create an empty dictionary with the keys being the rating, and the values being a list of players of that particular rating. Then sort that list according to the players’ market values. At last, for each rating, create a balanced Binary Search Tree (BST) (The tree will be balanced because I sorted the data and use the median as the root), so that when we search data later, it will retrieve data very fast. The trees will be stored using the list representation, which mean a leaf node would be [player, [], []]. The list is also stored as multiple json files, and a loadTree method is also provided in loadTree.py.

# Packages needed
resquests
json
BeautifulSoup
os
re
