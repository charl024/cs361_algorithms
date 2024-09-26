def bubbleSort(A):
    for i in range(len(A)):
        for j in range(len(A)):
            if A[i] < A[j]:
                temp = A[i]
                A[i] = A[j]
                A[j] = temp
    return A