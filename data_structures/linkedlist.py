class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertStart(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def removeStart(self):
        if self.head is None:
            return
        self.head = self.head.next

        

test = LinkedList()
test.insertStart(12)
test.insertStart(15)
test.insertEnd(9)

print(test.search(6))
print(test.search(13))
