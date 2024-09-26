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