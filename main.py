from loadTree import loadTree

# load trees from local machine
tree_82, tree_83, tree_84, tree_85, tree_86, tree_87, tree_88, tree_89, tree_90, tree_91, tree_92 = loadTree()

rating_list = ["82", "83", "84", "85", "86", "87", "88", "89", "90", "91", "92"]
# This function prints the search result (players infomation)
def print_result(player, concise=False):
    if(~concise):
        print("-----------------------------------")
        print("Name:", player["name"])
        print("Market Value:", player["price"])
        print("Postion:", player["position"])
        print("Club:", player["club"])
        print("League:", player["league"])
        print("nationality", player["nationality"])
        print("-----------------------------------")
        print("\n")
        print("\n")
        print("\n")
    else:
        print("-----------------------------------")
        print("Name:", player["name"])
        print("Market Value:", player["price"])
        print("-----------------------------------")
        print("\n")
        print("\n")

def inorder(tree, k, concise): # find the k smallest
    global c
    if tree == [] or c >= k:
        return
    inorder(tree[1],k,concise)
    if c == k:
        return
    print_result(tree[0], concise)
    c += 1
    
    inorder(tree[2],k, concise)


def reverse_inorder(tree, k, concise): # find the k largest
    global c    
    if tree == [] or c >= k:
        return
    reverse_inorder(tree[2], k, concise)
    if c == k:
        return
    print_result(tree[0], concise)
    c += 1
    reverse_inorder(tree[1], k, concise)

def yes2True(str):
    if str in ["yes", "Yes", "YES", "yep"]:
        return True
    elif str in ["No", "no", "nah", "nope"]:
        return False



while(True):
    print("Welcome to FIFA23 UT Chaapest by raing finder")
    invalid_rating = True
    while(invalid_rating):
        choice = input("please enter a player rating from 82 to 92:")
        if choice in rating_list:
            invalid_rating = False
            if choice == rating_list[0]:
                invalid_82 = True
                while(invalid_82):
                    print("Please select 1 of the 2 options:")
                    print("Enter 1 for k players with lowest market value")
                    print("Enter 2 for k players with highest maket value")
                    choice = input("please enter your choice:")
                    if choice == str(1):
                        k = int(input("please enter your k value:"))
                        concise = yes2True(input("Do you want the concise output?"))
                        c = 0
                        inorder(tree_82, k, concise)
                        invalid_82 = False
                    elif choice == str(2):
                        k = int(input("please enter your k value:"))
                        concise = yes2True(input("Do you want the concise output?"))
                        c = 0
                        reverse_inorder(tree_82, k, concise)
                        invalid_82 = False
                    else:
                        print("invalid choice!")
            elif choice == rating_list[1]:
                invalid_83 = True
                while(invalid_83):
                    print("Please select 1 of the 2 options:")
                    print("Enter 1 for k players with lowest market value")
                    print("Enter 2 for k players with highest maket value")
                    choice = input("please enter your choice:")
                    if choice == str(1):
                        k = int(input("please enter your k value:"))
                        concise = yes2True(input("Do you want the concise output?"))
                        c = 0
                        inorder(tree_83, k, concise)
                        invalid_83 = False
                    elif choice == str(2):
                        k = int(input("please enter your k value:"))
                        concise = yes2True(input("Do you want the concise output?"))
                        c = 0
                        reverse_inorder(tree_83, k, concise)
                        invalid_83 = False
                    else:
                        print("invalid choice!")
                        
            elif choice == rating_list[2]:
                invalid_84 = True
                while(invalid_84):
                    print("Please select 1 of the 2 options:")
                    print("Enter 1 for k players with lowest market value")
                    print("Enter 2 for k players with highest maket value")
                    choice = input("please enter your choice:")
                    if choice == str(1):
                        k = int(input("please enter your k value:"))
                        concise = yes2True(input("Do you want the concise output?"))
                        c = 0
                        inorder(tree_84, k, concise)
                        invalid_84 = False
                    elif choice == str(2):
                        k = int(input("please enter your k value:"))
                        concise = yes2True(input("Do you want the concise output?"))
                        c = 0
                        reverse_inorder(tree_84, k, concise)
                        invalid_84 = False
                    else:
                        print("invalid choice!")

            elif choice == rating_list[3]:
                invalid_85 = True
                while(invalid_85):
                    print("Please select 1 of the 2 options:")
                    print("Enter 1 for k players with lowest market value")
                    print("Enter 2 for k players with highest maket value")
                    choice = input("please enter your choice:")
                    if choice == str(1):
                        k = int(input("please enter your k value:"))
                        concise = yes2True(input("Do you want the concise output?"))
                        c = 0
                        inorder(tree_85, k, concise)
                        invalid_85 = False
                    elif choice == str(2):
                        k = int(input("please enter your k value:"))
                        concise = yes2True(input("Do you want the concise output?"))
                        c = 0
                        reverse_inorder(tree_85, k, concise)
                        invalid_85 = False
                    else:
                        print("invalid choice!")
            
            elif choice == rating_list[4]:
                invalid_86 = True
                while(invalid_86):
                    print("Please select 1 of the 2 options:")
                    print("Enter 1 for k players with lowest market value")
                    print("Enter 2 for k players with highest maket value")
                    choice = input("please enter your choice:")
                    if choice == str(1):
                        k = int(input("please enter your k value:"))
                        concise = yes2True(input("Do you want the concise output?"))
                        c = 0
                        inorder(tree_86, k, concise)
                        invalid_86 = False
                    elif choice == str(2):
                        k = int(input("please enter your k value:"))
                        concise = yes2True(input("Do you want the concise output?"))
                        c = 0
                        reverse_inorder(tree_86, k, concise)
                        invalid_86 = False
                    else:
                        print("invalid choice!")
            
            elif choice == rating_list[5]:
                invalid_87 = True
                while(invalid_87):
                    print("Please select 1 of the 2 options:")
                    print("Enter 1 for k players with lowest market value")
                    print("Enter 2 for k players with highest maket value")
                    choice = input("please enter your choice:")
                    if choice == str(1):
                        k = int(input("please enter your k value:"))
                        concise = yes2True(input("Do you want the concise output?"))
                        c = 0
                        inorder(tree_87, k, concise)
                        invalid_87 = False
                    elif choice == str(2):
                        k = int(input("please enter your k value:"))
                        concise = yes2True(input("Do you want the concise output?"))
                        c = 0
                        reverse_inorder(tree_87, k, concise)
                        invalid_87 = False
                    else:
                        print("invalid choice!")
            
            elif choice == rating_list[6]:
                invalid_88 = True
                while(invalid_88):
                    print("Please select 1 of the 2 options:")
                    print("Enter 1 for k players with lowest market value")
                    print("Enter 2 for k players with highest maket value")
                    choice = input("please enter your choice:")
                    if choice == str(1):
                        k = int(input("please enter your k value:"))
                        concise = yes2True(input("Do you want the concise output?"))
                        c = 0
                        inorder(tree_88, k, concise)
                        invalid_88 = False
                    elif choice == str(2):
                        k = int(input("please enter your k value:"))
                        concise = yes2True(input("Do you want the concise output?"))
                        c = 0
                        reverse_inorder(tree_88, k, concise)
                        invalid_88 = False
                    else:
                        print("invalid choice!")


            elif choice == rating_list[7]:
                invalid_89 = True
                while(invalid_89):
                    print("Please select 1 of the 2 options:")
                    print("Enter 1 for k players with lowest market value")
                    print("Enter 2 for k players with highest maket value")
                    choice = input("please enter your choice:")
                    if choice == str(1):
                        k = int(input("please enter your k value:"))
                        concise = yes2True(input("Do you want the concise output?"))
                        c = 0
                        inorder(tree_89, k, concise)
                        invalid_89 = False
                    elif choice == str(2):
                        k = int(input("please enter your k value:"))
                        concise = yes2True(input("Do you want the concise output?"))
                        c = 0
                        reverse_inorder(tree_89, k, concise)
                        invalid_89 = False
                    else:
                        print("invalid choice!")
            

            elif choice == rating_list[8]:
                invalid_90 = True
                while(invalid_90):
                    print("Please select 1 of the 2 options:")
                    print("Enter 1 for k players with lowest market value")
                    print("Enter 2 for k players with highest maket value")
                    choice = input("please enter your choice:")
                    if choice == str(1):
                        k = int(input("please enter your k value:"))
                        concise = yes2True(input("Do you want the concise output?"))
                        c = 0
                        inorder(tree_90, k, concise)
                        invalid_90 = False
                    elif choice == str(2):
                        k = int(input("please enter your k value:"))
                        concise = yes2True(input("Do you want the concise output?"))
                        c = 0
                        reverse_inorder(tree_90, k, concise)
                        invalid_90 = False
                    else:
                        print("invalid choice!")
            
            elif choice == rating_list[9]:
                invalid_91 = True
                while(invalid_91):
                    print("Please select 1 of the 2 options:")
                    print("Enter 1 for k players with lowest market value")
                    print("Enter 2 for k players with highest maket value")
                    choice = input("please enter your choice:")
                    if choice == str(1):
                        k = int(input("please enter your k value:"))
                        concise = yes2True(input("Do you want the concise output?"))
                        c = 0
                        inorder(tree_91, k, concise)
                        invalid_91 = False
                    elif choice == str(2):
                        k = int(input("please enter your k value:"))
                        concise = yes2True(input("Do you want the concise output?"))
                        c = 0
                        reverse_inorder(tree_91, k, concise)
                        invalid_91 = False
                    else:
                        print("invalid choice!")
            
            elif choice == rating_list[10]:
                invalid_92 = True
                while(invalid_92):
                    print("Please select 1 of the 2 options:")
                    print("Enter 1 for k players with lowest market value")
                    print("Enter 2 for k players with highest maket value")
                    choice = input("please enter your choice:")
                    if choice == str(1):
                        k = int(input("please enter your k value:"))
                        concise = yes2True(input("Do you want the concise output?"))
                        c = 0
                        inorder(tree_92, k, concise)
                        invalid_92 = False
                    elif choice == str(2):
                        k = int(input("please enter your k value:"))
                        concise = yes2True(input("Do you want the concise output?"))
                        c = 0
                        reverse_inorder(tree_92, k, concise)
                        invalid_92 = False
                    else:
             
                        print("invalid choice!")
            
        else:
            print("invalid choice, start over")
    choice = yes2True(input("Do you want to do it again?"))
    if(choice == True):
        continue
    else:
        break
print("Bye!")