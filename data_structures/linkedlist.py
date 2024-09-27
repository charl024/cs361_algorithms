class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertStart(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def insertEnd(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node

        currNode = self.head
        while (currNode.next):
            currNode = currNode.next

        currNode.next = node

    def removeStart(self):
        self.head = self.head.next            

    def search(self, data):
        currNode = self.head
        if currNode == None:
            return
        
        while (currNode.next):
            if currNode.data == data:
                return data
            currNode = currNode.next

        return    
