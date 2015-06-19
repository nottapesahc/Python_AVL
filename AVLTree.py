__author__ = 'stevenpatton'

class Node:
    def __init__(self):
        self.id = ''
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
        self.current = self.root

    def build(self, filename):
        file = open(filename, 'r')
        for line in file:
            # New node for each line
            node = Node()
            # break up the line and assign the id, data1 and data2 to the new node
            place_holder = 0
            for i in range(len(line)):
                if line[i] == ' ' and node.id == '':
                    node.id = line[0:i]
                    place_holder = i + 1
                if line[i] == ' ' and not (node.id == ''):
                    node.data1 = line[place_holder:i]
                    node.data2 = line[i + 1:len(line) - 1]

            a = 1
            self.insert(node)
        file.close()

    def insert(self, node):
        self.current = self.root
        while True:
            # First node will be set to root
            if self.root is None:
                self.root = node
                break

            # null condition left
            if self.current.id > node.id and self.current.leftChild is None:
                self.current.leftChild = node
                node.parent = self.current
                break

            # null condition right
            if self.current.id < node.id and self.current.rightChild is None:
                self.current.rightChild = node
                node.parent = self.current
                break

            # traversal cases
            else:
                if self.current.id < node.id:
                    self.current = self.current.rightChild
                if self.current.id > node.id:
                    self.current = self.current.leftChild



# run
a = AVLTree()
a.build("SuperImportantData.txt")