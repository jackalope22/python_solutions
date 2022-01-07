
class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insertData(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insertData(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insertData(data)
        else:
            self.data = data

    def findVal(self, findVal):
        if findVal < self.data:
            if self.left is None:
                return str(findVal)+" Not Found"
            return self.left.findVal(findVal)
        elif findVal > self.data:
            if self.right is None:
                return str(findVal)+" Not Found"
            return self.right.findVal(findVal)
        else:
            print(str(self.data) + " is found")

    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data),
        if self.right:
            self.right.printTree()

#look into deletion function for tree

root = Node(12)
root.insertData(6)
root.insertData(14)
root.insertData(3)
root.insertData(10)
root.insertData(16)
root.insertData(7)
root.insertData(12)
print(root.findVal(7))
print(root.findVal(14))
root.printTree()