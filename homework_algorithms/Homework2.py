# HOMEWORK 2

# Problem 1:
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 2) + fibonacci(n - 1)

# Problem 2:
def towersOfHanoi(n, firstRod, secondRod, thirdRod):
    if n == 0:
        return
    towersOfHanoi(n - 1, firstRod, thirdRod, secondRod)
    print("disk ", n," moved from ", firstRod, " to ", secondRod)
    towersOfHanoi(n - 1, thirdRod, secondRod, firstRod)

# Problem 3:
def diagonalSort(A):
    m = len(A)
    n = len(A[0])

    # sorts the diagonals that start from the column side
    for c in range(0, n-1):
        sortDiagonal(A, 0, c, m, n)

    # sorts the diagionals that start from the row side 
    for r in range(0, m-1):
        sortDiagonal(A, r, 0, m, n)    

    return A

# implementation of bubble sort as a helper function
def bubbleSort(A):
    for i in range(len(A)):
        for j in range(len(A)):
            if A[i] < A[j]:
                temp = A[i]
                A[i] = A[j]
                A[j] = temp
    return A

def sortDiagonal(A, row, col, m, n):
    diagonal = []
    currRow, currCol = row, col
    # iterate through matrix and turn diagonals into arrays
    while currRow < m and currCol < n:
        diagonal.append(A[currRow][currCol])
        currRow += 1
        currCol += 1
    
    # sort diagonal (any sorting algorithm)
    diagonal = bubbleSort(diagonal)

    # put the sorted diagonal back into the matrix
    currRow, currCol = row, col
    index = 0
    while currRow < m and currCol < n:
        A[currRow][currCol] = diagonal[index]
        currRow += 1
        currCol += 1
        index += 1

# Problem 4
def radix_sort_variable_strings(A):

    # gets length of longest string in array
    k = get_longest_strlen(A)

    #total amount of ascii values
    ascii_num = 256

    # Create an array B of 10 buckets, each bucket is a queue
    buckets = [[] for _ in range(ascii_num + 1)]

    # iterates backwards from k
    for j in range(k - 1, -1, -1):
        for str in A:
            if len(str) > j:
                char_value = ord(str[j])
                buckets[char_value].append(str)
            else:
                buckets[0].append(str)

        # dequeue from each bucket and put back into array
        i = 0
        for bucket in buckets:
            while bucket:
                A[i] = bucket.pop(0)  # Dequeue from the bucket
                i += 1

    return A

# helper function to get length of longest string in array
def get_longest_strlen(A):
    maxLen = -1
    for str in A:
        if len(str) > maxLen:
            maxLen = len(str)

    return maxLen

# Problem 6
def minHeapCombine(A, B):
    # min heaps as arrays
    # combine min heaps together
    res = A + B
    turnArrayIntoHeap(res)
    return res

def turnArrayIntoHeap(A):
    length = len(A)
    n = (length//2) - 1
    # loops backwards, heapifies the array
    for i in range(n, -1, -1):
        minHeapify(A, length, i)

def minHeapify(A, n, index):
    # if index is more than n, then exit function
    if (index >= n):
        return
    # left child of parent
    leftNode = 2 * index + 1
    # right child of parent
    rightNode = 2 * index + 2
    leastIndex = index

    # sets leastIndex
    if leftNode < n and A[leftNode] < A[leastIndex]:
        leastIndex = leftNode

    # sets leastIndex
    if rightNode < n and A[rightNode] < A[leastIndex]:
        leastIndex = rightNode

    # swap and call heapify again
    if leastIndex != index: 
        temp = A[leastIndex]
        A[leastIndex] = A[index]
        A[index] = temp
        minHeapify(A, n, leastIndex)

# Problem 7
# implementation of stack
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, a):
        self.stack.append(a)

    def peek(self):
        return self.stack[-1]
    
    def pop(self):
        if len(self.stack) == 0:
            return None
        res = self.stack[-1]
        self.stack = self.stack[:-1]
        return res
    
    def isEmpty(self):
        return len(self.stack) == 0

    def print(self):
        print(self.stack)

# implementation of queue using two stacks
class QueueMadeFromStacks:
    def __init__(self):
        self.stackOne = Stack()
        self.stackTwo = Stack()

    def enqueue(self, data):
        if self.stackOne.isEmpty():
            # if stackOne is empty, push data to stackOne
            self.stackOne.push(data)
        else:
            # move all the contents of stackOne to stackTwo
            for obj in self.stackOne.stack:
                n = self.stackOne.pop()
                self.stackTwo.push(n)
            # push data to stackOne    
            self.stackOne.push(data)
            # move back all the data from stackTwo back to stackOne
            for obj in self.stackTwo.stack:
                n = self.stackTwo.pop()
                self.stackOne.push(n)

    def dequeue(self):
        return self.stackOne.pop()    

    def isEmpty(self):
        return self.stackOne.isEmpty() and self.stackTwo.isEmpty()
    
    def printQueue(self):
        for obj in self.stackOne.stack:
            print(obj, end=" ")

# Problem 8
def permutationOrder(A, permutation):
    n = len(A)
    # for i from 0 to n-1
    for i in range(0, n):
        while permutation[i] != i:
            tempA = A[i]
            A[i] = A[permutation[i]]
            A[permutation[i]] = tempA

            tempPerm = permutation[i]
            permutation[i] = permutation[permutation[i]]
            permutation[tempPerm] = tempPerm

# Problem 10
# Implementation of a LinkedList using a Node object
class LinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def mergeSortedLists(A: LinkedListNode, B: LinkedListNode) -> LinkedListNode:
    # if the first node of A has a larger value than B, then the current node is A otherwise B
    if A.data <= B.data:
        mergedHead = A
        A = A.next
    else:
        mergedHead = B
        B = B.next

    currNode = mergedHead

    # while A and B are valid
    while A != None and B != None:
        # if nodeA is less than nodeB, then set the current node's next to be node A otherwise set B
        if A.data < B.data:
            currNode.next = A
            A = A.next
        else:
            currNode.next = B
            B = B.next
        # move to current node's next    
        currNode = currNode.next
        
    # once while loop ends, append the remaining nodes from remaining list
    if A != None:
        currNode.next = A
    elif B != None:
        currNode.next = B

    # return the head of the merged linked list
    return mergedHead       










# Code to test algorithms:
print()

# Problem 1 Test
print("PROBLEM 1 TEST: ")
print("fibonacci(5): ")
print(fibonacci(5))
print("fibonacci(9): ")
print(fibonacci(9))
print("fibonacci(21): ")
print(fibonacci(21))
print()

# Problem 2 Test
print("PROBLEM 2 TEST: ")
towersOfHanoi(3, "ONE", "TWO", "THREE")
print()

# Problem 3 Test
print("PROBLEM 3 TEST: ")

A = [[3, 3, 1, 1], [2, 2, 1, 2], [1, 1, 1, 2]]

print("Before diagonal sort: ")

for i in range(len(A)):
    print(A[i])
newA = diagonalSort(A)

print("After diagonal sort: ")

for i in range(len(newA)):
    print(newA[i])
print()

# Problem 4 Test
print("PROBLEM 4 TEST: ")
B = ["where","am","isn't","actually","federation","i","growing","short","long"]
print("Before modified radix sort: ")
print(B)
print("After modified radix sort: ")
print(radix_sort_variable_strings(B))    
print()

# Problem 6 Test
print("PROBLEM 6 TEST: ")
print("Before min heap combine: ")
C1 = [5, 4, 5, 2, 3, 1]
C2 = [234, 2, 46, 12, 765, 90, 1, 5, 3, 99, 34, 65]
print(C1)
print(C2)
C = minHeapCombine(C1, C2)
print(C)
print()

#Problem 7 Test
print("PROBLEM 7 TEST: ")
newQueue = QueueMadeFromStacks()
newQueue.enqueue(5)
newQueue.enqueue(7)
newQueue.enqueue(6)
newQueue.printQueue()
newQueue.dequeue()
print()
newQueue.printQueue()
newQueue.dequeue()
print()
newQueue.printQueue()
newQueue.dequeue()
print()
newQueue.printQueue()
print()

# Problem 8 Test
# Using the example given in the homework, but since Python uses zero-indexed arrays
# I convert the example permutation into a zero-indexed version which is then passed
# into the algorithm.
print("PROBLEM 8 TEST: ")
D = [10.5, 9.3, 2.7, 13.6]
permutationOneIndexed = [4, 2, 3, 1]
permutationZeroIndexed = [i - 1 for i in permutationOneIndexed]

print("Before permutation reorder: ")
print(D)
permutationOrder(D, permutationZeroIndexed)
print("After permutation reorder: ")
print(D)
print()

# Problem 10 test
# Using helper functions createLinkedList to create a linked list using nodes
# and function printLinkedList to print list out into the terminal
print("PROBLEM 10 TEST: ")

def createLinkedList(elements):
    if not elements:
        return None
    head = LinkedListNode(elements[0])
    current = head
    for data in elements[1:]:
        current.next = LinkedListNode(data)
        current = current.next
    return head

def printLinkedList(head):
    current = head
    while current:
        print(current.data, end=' ')
        current = current.next
    print()

# Using the example from the homework: 
listA = createLinkedList([1, 2, 4])
listB = createLinkedList([1, 3, 4])
mergedList = mergeSortedLists(listA, listB)
printLinkedList(mergedList)