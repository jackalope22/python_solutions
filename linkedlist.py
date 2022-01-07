class Node:

    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = Node()

    def append(self, data):
        new_node = Node(data)
        current = self.head
        while current.next != None:
            current = current.next
        current.next = new_node

    def length(self):
        current = self.head
        total = 0
        while current.next!=None:
            total+=1
            current = current.next
        return total

    def display(self):
        elements = []
        current_node = self.head
        while current_node.next != None:
            current_node=current_node.next
            elements.append(current_node.data)
        print(elements)

    def get(self, index):
        if index >= self.length():
            print("get index out of range")
            return None
        current_index = 0
        current_node = self.head
        while True:
            current_node = current_node.next
            if current_index == index:
                return current_node.data
            current_index += 1


my_list = LinkedList()

my_list.display()

my_list.append(1)
my_list.append(5)
my_list.append(10)
my_list.append(25)
my_list.append(7)
my_list.append(3)
my_list.append(30)

my_list.display()

print(f"value at index 3: {my_list.get(3)}")
