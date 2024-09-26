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


def sortDiagonal(A, row, col, m, n):
    diagonal = []
    currRow, currCol = row, col
    while currRow < m and currCol < n:
        diagonal.append(A[currRow][currCol])
        currRow += 1
        currCol += 1
    
    diagonal.sort()

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

def get_longest_strlen(A):
    maxLen = -1
    for str in A:
        if len(str) > maxLen:
            maxLen = len(str)

    return maxLen

# Code to test algorithms:

# Problem 1 Test
print("Fibonacci test: ")
print("fibonacci(5): ")
print(fibonacci(5))
print("fibonacci(9): ")
print(fibonacci(9))
print("fibonacci(21): ")
print(fibonacci(21))

#Problem 2 Test
print("Towers of Hanoi test: ")
towersOfHanoi(3, "ONE", "TWO", "THREE")

# Problem 3 Test
A = [[3, 3, 1, 1], [2, 2, 1, 2], [1, 1, 1, 2]]
newA = diagonalSort(A)

for i in range(len(newA)):
    print(newA[i])

#Problem 4 Test
A = ["where","am","isn't","actually","federation","i","growing","short","long"]
print(radix_sort_variable_strings(A))    