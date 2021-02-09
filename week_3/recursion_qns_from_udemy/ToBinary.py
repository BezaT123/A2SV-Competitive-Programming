def to_binary_iterative(num):
    ans =""
    while num != 0:
        remainder = num % 2
        num = num //2
        ans = str(remainder) + ans
    return ans

def to_binary_recursive(num):
    # if num == 0:
    #     return ""
    # l.append(num % 2)
    # to_binary_recursive(num//2,l)
    # return l
    if num == 0:
        return ""
    return to_binary_recursive(num //2) + str(num % 2) 

print(to_binary_recursive(8))