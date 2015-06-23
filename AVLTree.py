__author__ = 'stevenpatton'

class Node:
    def __init__(self):
        self.id = 0
        self.data1 = ''
        self.data2 = ''
        self.parent = None
        self.leftChild = None
        self.rightChild = None

    def display(self):
        return self.id + " " + self.data1 + " " + self.data2


class AVLTree:
    def __init__(self):
        self.root = None

    def build(self, filename):
        file = open(filename, 'r')
        a = 0
        for line in file:
            # New node for each line
            node = Node()
            # break up the line and assign the id, data1 and data2 to the new node
            place_holder = 0
            for i in range(len(line)):
                if line[i] == ' ' and node.id == 0:
                    tmp = line[0:i]
                    node.id = int(tmp)
                    place_holder = i + 1
                if line[i] == ' ' and not (node.id == 0):
                    node.data1 = line[place_holder:i]
                    node.data2 = line[i + 1:len(line) - 1]

            if not(node.id == 0):
                self.insert(node, self.root)
                a += 1
        file.close()

    def insert(self, new_node, current):
        if self.root is None:
            self.root = new_node
            return
        if not(current.leftChild is None) and current.id > new_node.id:
            return self.insert(new_node, current.leftChild)
        if not(current.rightChild is None) and current.id < new_node.id:
            return self.insert(new_node, current.rightChild)
        if current.id > new_node.id:
            current.leftChild = new_node
            new_node.parent = current
        if current.id < new_node.id:
            current.rightChild = new_node
            new_node.parent = current




# run
a = AVLTree()
a.build("SuperImportantData.txt")