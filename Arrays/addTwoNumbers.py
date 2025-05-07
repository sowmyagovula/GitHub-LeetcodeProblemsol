def addTwoNumbers(l1, l2):
    carry = 0
    result = [] 

    l1 = l1[::-1]
    l2 = l2[::-1]
    max_len = (max(len(l1), len(l2)))
    for i in range(max_len):
        x = l1[i] if i < len(l1) else 0
        y = l2[i] if i < len(l2) else 0
        total = x + y + carry
        carry = total //10
        result.append(total % 10)

    if carry:
        result.append(carry)
    return result[::-1]


l1 = [7,2,4,3]
l2 = [5,6,4]
Output = [7,8,0,7]

print(addTwoNumbers(l1, l2))