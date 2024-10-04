def reverse(word):
    stack = []
    for c in word:
        stack.append(c)

    res = ""    
    while (len(stack) != 0):
        c = stack.pop()
        res += c

    return res

print(reverse("hello world"))      