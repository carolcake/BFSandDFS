# Caroline Hsu - 9/26/2022
# This program utilizes tree data structures to implement breadth first search and depth first search. This program
# utilizes recusion and queues for bfs and dfs and will output the full path from the root to the file when searching
# for a specific extension.

class TreeNode:
    # node constructor (children must be a list bc the node can have multiple children)
    def __init__(self, p, n):
        self.path = p
        self.children = []
        self.name = n
        
# class tree
class Tree:
    # constructor for tree
    def __init__(self, r):
        self.root = TreeNode(None, r)
    
    # receives the path and n (name) to add node
    def addNode(self, path, n):
        # split the pathlist by adding /
        pathList = path.split("/")
        # make a temp root and create new variable for directory 
        temp = self.root
        directoryIsValid = True
        # for loop for each directory in the path list (separated by /)
        for directory in pathList:
            # if the directory doesn't equal the name of the temp (empty too)
            if directory != temp.name and directory != "":
                # make another if statement for if there are no children 
                if temp.children == []:
                    # loop through the children of the temp to see if the directory has no subfolders 
                    for child in temp.children:
                        print("directory has no subfolders")
                        directoryIsValid = False
                        break
                # if children temp has stuff in the list
                else:
                    # set child exists to false, loop through children and if the directory is = to the child name
                    childExists = False
                    for child in temp.children:
                        if directory == child.name:
                            # add children and set child exists to true
                            childExists = True
                            temp = temp.children[temp.children.index(child)]
                    # if the child exists is false then print that the directory cannot be found
                    if childExists == False:
                        print("directory is not found")
                        break
        # if the directory directory is valid, then insert node 
        if directoryIsValid == True:
            print("inserting node")
            node = TreeNode(path, n)
            temp.children.append(node)
    # dfs - needs node and extension
    def depthFirstSearch(self, node, extension):
        # recursive call
        # if the children has a list 
        if node.children != []:
            # loop through each child in the children node and use recursion 
            for child in node.children:
                self.depthFirstSearch(child, extension)
        # base case
        else:
            # if the extension is in the node name, then print the path with the slashes
            if extension in node.name:
                print(node.path + "/" + node.name)
    # bfs - needs extension
    def breadthFirstSearch(self, extension):
        # declare queue of the root 
        queue = [self.root]
        # while the queue is not empty
        while queue != []:
            # pop the queue and set the temp equal to it
            temp = queue.pop(0)
            # if the temp children is an empty list
            if temp.children == []:
                # if the extension is in the temp name, then print the path with the slashes
                if extension in temp.name:
                    print(temp.path + "/" + temp.name)
            else:
                # for child in the children of the temp, append the child to the queue
                for child in temp.children:
                    queue.append(child)

def main():
    # create a tree and add nodes to the tree
    myTree = Tree("Users")
    myTree.addNode("/Users", "carolinehsu")
    myTree.addNode("/Users/carolinehsu", "downloads")
    myTree.addNode("/Users/carolinehsu", "documents")
    myTree.addNode("/Users/carolinehsu/documents", "government documents")
    myTree.addNode("/Users/carolinehsu/documents/government documents", "adoptionpapers.pdf")
    myTree.addNode("/Users/carolinehsu/documents/government documents", "lawsuit.pdf")
    myTree.addNode("/Users/carolinehsu/documents/government documents", "taxes.pdf")
    myTree.addNode("/Users/carolinehsu/documents/government documents", "scam.pdf")
    myTree.addNode("/Users/carolinehsu/documents/government documents", "fafsa.pdf")
    myTree.addNode("/Users/carolinehsu/documents", "books")
    myTree.addNode("/Users/carolinehsu/documents/books", "ofmiceandmen.pdf")
    myTree.addNode("/Users/carolinehsu/documents/books", "littlewomen.pdf")
    myTree.addNode("/Users/carolinehsu/documents/books", "night.pdf")
    myTree.addNode("/Users/carolinehsu/documents/books", "float.pdf")
    myTree.addNode("/Users/carolinehsu/documents/books", "thehateugive.pdf")
    myTree.addNode("/Users/carolinehsu/documents/books", "whyshedisappeared.png")
    myTree.addNode("/Users/carolinehsu/documents", "")
    myTree.addNode("/Users/carolinehsu/downloads", "images")
    myTree.addNode("/Users/carolinehsu/downloads/images", "cats")
    myTree.addNode("/Users/carolinehsu/downloads/images/cats", "kirby.png")
    myTree.addNode("/Users/carolinehsu/downloads/images/cats", "lily.png")
    myTree.addNode("/Users/carolinehsu/downloads/images/cats", "schubert.png")
    myTree.addNode("/Users/carolinehsu/downloads/images/cats", "trixie.png")
    myTree.addNode("/Users/carolinehsu/downloads/images", "dogs")
    myTree.addNode("/Users/carolinehsu/downloads/images/dogs", "charlie.png")
    myTree.addNode("/Users/carolinehsu/downloads/images/dogs", "ryan.png")
    myTree.addNode("/Users/carolinehsu/downloads", "11th grade")
    myTree.addNode("/Users/carolinehsu/downloads/11th grade", "ib comp sci hl")
    myTree.addNode("/Users/carolinehsu/downloads/11th grade/ib comp sci hl", "topic4.pdf")
    myTree.addNode("/Users/carolinehsu/downloads/11th grade/ib comp sci hl", "topic1.pdf")
    myTree.addNode("/Users/carolinehsu/downloads/11th grade/ib comp sci hl", "topic2.pdf")
    myTree.addNode("/Users/carolinehsu/downloads/11th grade/ib comp sci hl", "topicoop.pdf")
    myTree.addNode("/Users/carolinehsu/downloads/11th grade", "ib aa hl")
    myTree.addNode("/Users/carolinehsu/downloads/11th grade/ib aa hl", "calculus.pdf")
    myTree.addNode("/Users/carolinehsu/downloads/11th grade/ib aa hl", "series.pdf")
    myTree.addNode("/Users/carolinehsu/downloads/11th grade/ib aa hl", "cry.png")
    myTree.addNode("/Users/carolinehsu/downloads/11th grade", "ib bio hl")
    myTree.addNode("/Users/carolinehsu/downloads/11th grade/ib bio hl", "plants.pdf")
    myTree.addNode("/Users/carolinehsu/downloads/11th grade/ib bio hl", "metabolism.pdf")
    myTree.addNode("/Users/carolinehsu/downloads/11th grade/ib bio hl", "ecology.pdf")
    myTree.addNode("/Users/carolinehsu/downloads/11th grade/ib bio hl", "cells.pptx")
    myTree.addNode("/Users/carolinehsu/downloads/11th grade/ib bio hl", "water.pptx")
    myTree.addNode("/Users/carolinehsu/downloads/11th grade/ib bio hl", "membrane.pptx")
    myTree.addNode("/Users/carolinehsu/downloads/11th grade/ib bio hl", "mitosis.pptx")
    myTree.addNode("/Users/carolinehsu/downloads", "12th grade")
    myTree.addNode("/Users/carolinehsu/downloads/12th grade", "death")
    myTree.addNode("/Users/carolinehsu/downloads/12th grade/death", "college apps")
    myTree.addNode("/Users/carolinehsu/downloads/12th grade/death/college apps", "stanford.pdf")
    myTree.addNode("/Users/carolinehsu/downloads/12th grade/death/college apps", "harvard.pdf")
    myTree.addNode("/Users/carolinehsu/downloads/12th grade/death/college apps", "rice.pdf")
    myTree.addNode("/Users/carolinehsu/downloads/12th grade/death/college apps", "columbia.docx")
    myTree.addNode("/Users/carolinehsu/downloads/12th grade/death/college apps", "brown.docx")
    
    # print dfs and bfs search looking for .pdf extensions
    print("DFS Search:")
    myTree.depthFirstSearch(myTree.root, ".pdf")
    print("BFS Search:")
    myTree.breadthFirstSearch(".pdf")
    
# run main class
main()