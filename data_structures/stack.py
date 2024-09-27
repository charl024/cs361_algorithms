class Stack:

    def __init__(self):
        self.stack = []

    def push(self, a):
        self.stack.append(a)

    def peek(self):
        return self.stack[-1]
    
    def pop(self):
        res = self.stack[-1]
        self.stack = self.stack[:-1]
        return res
    
    def isEmpty(self):
        return len(self.stack) == 0

    def print(self):
        print(self.stack)


# testing
test = Stack()
test.push(56)
test.print()
print(test.isEmpty())
print(test.pop())
print(test.isEmpty())
test.print()