def radix_sort_variable_strings(A, n, k):
    # Create an array B of 10 buckets, each bucket is a queue
    buckets = [[] for _ in range(10)]

    for j in range(k):
        for n in A:
            digit = (n // (10 ** j)) % 10
            buckets[digit].append(n)

        i = 0
        for bucket in buckets:
            while bucket:
                A[i] = bucket.pop(0)  # Dequeue from the bucket
                i += 1

    return A    