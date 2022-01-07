class Node:
    def __init__(self, value, next_value=None):
        self.value = value
        self.next_value = next_value

    #get the value
    def get_value(self):
        return self.value

    #get the next value
    def get_next_value(self):
        return self.next_value

class LinkedList:
    def __init__(self):
        self.start = None

    def printStops(self):
        stoplist = ""
        current_stop = self.start
        while current_stop:
            if current_stop != None:
                stoplist += str(current_stop.get_value()) + " "
            current_stop = current_stop.next_value
        return stoplist


travel = LinkedList()
travel.start = Node("pittsburgh")
stop1 = Node("newyork")
stop2 = Node("london")
travel.start.next_value = stop1
stop1.next_value = stop2
print(travel.printStops())

