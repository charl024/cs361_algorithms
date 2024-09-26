# A - array to sort
def radix_sort_variable_strings(A):

    k = get_longest_strlen(A)

    # Create an array B of 10 buckets, each bucket is a queue
    ascii_num = 256
    buckets = [[] for _ in range(ascii_num + 1)]

    for j in range(k - 1, -1, -1):
        for str in A:
            if len(str) > j:
                char_value = ord(str[j])
                buckets[char_value].append(str)
            else:
                buckets[0].append(str)

        i = 0
        for bucket in buckets:
            while bucket:
                A[i] = bucket.pop(0)  # Dequeue from the bucket
                i += 1

    return A

def get_longest_strlen(A):
    maxLen = -1
    for str in A:
        if len(str) > maxLen:
            maxLen = len(str)

    return maxLen


A = ["where","am","isn't","actually","federation","i","growing","short","long"]
print(radix_sort_variable_strings(A))