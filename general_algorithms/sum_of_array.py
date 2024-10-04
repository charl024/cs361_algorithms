def sumOfArray(A, n):
    if n == 0:
        return 0
    return sumOfArray(A, n - 1) + A[n - 1]

A = [1, 2, 3, 4, 5, 6]
sum = sumOfArray(A, len(A))
print(sum)