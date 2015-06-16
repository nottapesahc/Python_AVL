__author__ = 'stevenpatton'


class Node:
    def __init__(self):
        self.id = "abc"
        self.data1 = 0
        self.data2 = 0
        self.parent = None
        self.leftChild = None
        self.rightChild = None

    def display(self):
        return self.id + " " + self.data1 + " " + self.data2


class AVLTree:
    def __init__(self):
        self.root = None
        self.current = None

    def build(self, filename):
        file = open(filename, 'r')
        for line in file:
            print(line)
        file.close()

a = AVLTree()
a.build("data.txt")