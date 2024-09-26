#HOMEWORK 2

#Problem 1:
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 2) + fibonacci(n - 1)

#Problem 2:
def towersOfHanoi(n, firstRod, secondRod, thirdRod):
    if n == 0:
        return
    towersOfHanoi(n - 1, firstRod, thirdRod, secondRod)
    print("disk ", n," moved from ", firstRod, " to ", secondRod)
    towersOfHanoi(n - 1, thirdRod, secondRod, firstRod)

#Problem 3:
def diagonalSort(A):
    m = len(A)
    n = len(A[0])

    for c in range(0, n-1):
        sortDiagonal(A, 0, c, m, n)

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



# code to test algorithms
print("Fibonacci test: ")
print(fibonacci(5))

print("Towers of Hanoi test: ")
towersOfHanoi(3, "ONE", "TWO", "THREE")

A = [[3, 3, 1, 1], [2, 2, 1, 2], [1, 1, 1, 2]]
newA = diagonalSort(A)

for i in range(len(newA)):
    print(newA[i])