def ValidParentheses(s):
    check = {')':'(', ']':'[', '}':'{'}
    stack = []

    for i in s:
        if i in check.values():
            stack.append(i)
        elif i in check.keys():
            if stack[-1] == check[i]:
                stack.pop()
            else:
                return False
        else:
            continue #return false
    return not stack
        

s = "(a)[b]{c}"
Output= True

print(ValidParentheses(s))
print(ValidParentheses(s)==Output)