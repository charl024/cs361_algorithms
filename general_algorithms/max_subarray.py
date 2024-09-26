import math

def cross_subarray(A, low, mid, high):
    lsum = -2147483647
    rsum = -2147483647
    maxright = 0
    maxleft = 0
    sum = 0
    i = mid
    while (i >= low):
        sum = sum + A[i]
        if sum > lsum:
            lsum = sum
            maxleft = i

        i -= 1

    sum = 0

    j = mid + 1

    while (j < high):
        sum = sum + A[j]
        if sum > rsum:
            rsum = sum
            maxright = j
        j += 1

    csum = lsum + rsum
    return maxleft, maxright, csum


def max_subarray(A, low, high):
    if low == high:
        return A, low, high
    else:
        mid = math.floor((low + high)/2)
        llow, lhigh, lsum = max_subarray(A, low, mid)
        hlow, hhigh, rsum = max_subarray(A, mid+1, high)
        clow, chigh, csum = cross_subarray(A, low, mid, high)
        
        if lsum >= rsum and lsum >= csum:
            return llow, lhigh, lsum
        elif rsum >= lsum and rsum >= csum:
            return hlow, hhigh, rsum
        else:
            return clow, chigh, csum