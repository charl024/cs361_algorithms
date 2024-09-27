from insertion_sort_iterative import insertionSortIterative
def bucket_sort(A):
    n = len(A)
    B = [[] for _ in range(n)]

    for j in A:
        r = int(n * j)
        B[r].append(j)

    for bucket in B:
        insertionSortIterative(bucket)

    index = 0
    for bucket in B:
        for i in bucket:
            A[index] = i
            index += 1

A = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]

bucket_sort(A)
print(A)
