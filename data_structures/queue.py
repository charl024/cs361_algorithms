class Queue:

    def __init__(self):
        self.queue = []

    def enqueue(self, a):
        self.queue.append(a)

    def dequeue(self):
        res = self.queue[0]
        self.queue.remove(res)
        return res
    
    def front(self):
        return self.queue[0]
    
    def isEmpty(self):
        return len(self.queue) == 0

    def print(self):
        print(self.queue)

#testing
test = Queue()
print(test.isEmpty())
test.print()
test.enqueue(6)
test.print()
test.enqueue(7)
test.print()
f = test.dequeue()
print(f)
test.print()
print(test.front())