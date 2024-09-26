def insertionSortIterative(A):
    n = len(A)

    if n <= 1:
        return
    
    for i in range(1, n):
        key = A[i]
        j = i - 1
        while j >= 0 and key < A[j]:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = key  

    return A   