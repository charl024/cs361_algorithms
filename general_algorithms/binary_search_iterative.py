import math

def binarySearchIterative(A, target):
    low = 0
    high = len(A) - 1
    while low <= high:
        mid = math.ceil((low + high)/2)
        num = A[mid]
        if target == num:
            return mid
        elif target > num:
            low = mid + 1
        elif target < num:
            high = mid

    return -1    