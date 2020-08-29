'''
Ryan Balog
CS2420
Project 5
'''
from binarysearchtree import BinarySearchTree

VALUES = [21, 26, 30, 9, 4, 14, 28, 18, 15, 10, 2, 3, 7]
REMOVABLES = [21, 9, 4, 18, 15, 7]


def main():
    '''Driver for program'''
    tree = BinarySearchTree()
    for val in VALUES:
        tree.add(val)


    for item in tree.preorder():
        print(item, end=", ")
    print("\n")
    print(tree)
    for item in REMOVABLES:
        tree.remove(item)

    print(tree)


if __name__ == "__main__":
    main()
