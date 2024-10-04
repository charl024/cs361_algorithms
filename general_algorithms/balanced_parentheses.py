def balancedParentheses(A):
    stack = []
    for c in A:
        if (c == '(' or c == '[' or c == '{'):
            stack.append(c)
        elif (c == ')' or c == ']' or c == ']'):
            if (len(stack) == 0):
                return False
            stack.pop()
    return len(stack) == 0

A = "[()()]"
print(balancedParentheses(A))