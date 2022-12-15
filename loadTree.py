import json
def loadTree():
    with open("82_tree.json", "r") as openfile:
        tree_82 = json.load(openfile)
    with open("83_tree.json", "r") as openfile:
        tree_83 = json.load(openfile)
    with open("84_tree.json", "r") as openfile:
        tree_84 = json.load(openfile)
    with open("85_tree.json", "r") as openfile:
        tree_85 = json.load(openfile)
    with open("86_tree.json", "r") as openfile:
        tree_86 = json.load(openfile)
    with open("87_tree.json", "r") as openfile:
        tree_87 = json.load(openfile)
    with open("88_tree.json", "r") as openfile:
        tree_88 = json.load(openfile)
    with open("89_tree.json", "r") as openfile:
        tree_89 = json.load(openfile)
    with open("90_tree.json", "r") as openfile:
        tree_90 = json.load(openfile)
    with open("91_tree.json", "r") as openfile:
        tree_91 = json.load(openfile)
    with open("92_tree.json", "r") as openfile:
        tree_92 = json.load(openfile)
    
    return tree_82, tree_83, tree_84, tree_85, tree_86, tree_87, tree_88, tree_89, tree_90, tree_91, tree_92

