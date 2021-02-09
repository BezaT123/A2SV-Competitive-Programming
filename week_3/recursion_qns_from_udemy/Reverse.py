def reverse(s):
    p = ""
    for i in range(len(s)-1,-1,-1):
        p = p + s[i]
    return p

def recursiveReverse(s):
    if s == '':
        return s
    return s[len(s)-1] + recursiveReverse(s[:len(s)-1])

print(recursiveReverse("appmillers"))