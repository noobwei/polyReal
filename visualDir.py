# Importing Libraries
from directory_tree import DisplayTree
import os

# Main Method
if __name__ == '__main__':
    directoryPath = os.getcwd()
    DisplayTree(directoryPath)