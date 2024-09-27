def counting_sort(A):
    # get length of input array
    n = len(A)

    # find max value in input array
    max = -1*(2 << 16)
    for num in A:
        if max < num:
            max = num

    # initialize counting array and output array
    countarr = [0] * (max + 1)
    outarr = [0] * (len(A))

    # count each digit in the input array by incrementing elements in counting array
    for num in A:
        countarr[num] += 1

    # loop through counting array and add sum each element with the value before it
    for i in range(1, max+1):
        countarr[i] += countarr[i - 1]

    # sorts digits by using the cumulative sums in counting array as index numbers in output array, putting the index of the cumulative sums as the elements in the output array
    for i in range(len(A) - 1, -1, -1):
        outarr[countarr[A[i]] - 1] = A[i]
        countarr[A[i]] -= 1

    return outarr

A = [3,1,4,5,12,8,4,9]

print(counting_sort(A))         



