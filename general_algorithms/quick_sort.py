def quicksort(A, start, end):
    if start >= end:
        return
    pivot = partition(A, start, end)
    quicksort(A, start, pivot - 1)
    quicksort(A, pivot + 1, end)

def partition(A, start, end):
    pivot = A[end]
    i = start - 1
    for j in range(start, end):
        if A[j] < pivot:
            i += 1
            temp = A[i]
            A[i] = A[j]
            A[j] = temp

    i += 1
    temp = A[i]
    A[i] = A[end]
    A[end] = temp

    return i

A = [3,1,4,5,12,8,4,9]
quicksort(A, 0, len(A) - 1)
print(A)