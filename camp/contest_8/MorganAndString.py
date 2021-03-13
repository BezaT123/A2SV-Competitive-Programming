# Complete the morganAndString function below.
def morganAndString(a, b):
    i = j = 0
    max_len = max(len(a),len(b))
    result = ""

    while True:
        if i >= len(a) and j >= len(b):
            break
        if i >= len(a):
            result +=b[j]
            j += 1
            continue
        if  j >= len(b):
            result += a[i]
            i += 1
            continue
        if a[i] > b[j]:
            result += b[j]
            j += 1
        elif a[i] < b[j]:
            result += a[i]
            i += 1
        else:
            isASmaller = True
            k = i + 1
            l = j + 1
            while k < len(a) and l < len(b):
                if a[k] > b[l]:
                    isASmaller = False
                    break
                if a[k] < b[l]:
                    isASmaller = True
                    break
                k += 1
                l += 1

            if isASmaller:
                result += a[i]
                i += 1
            else:
                result += b[j]
                j += 1
            # if a[i:] > b[j:]:
            #     result += b[j]
            #     j += 1
            # else:
            #     result += a[i]
            #     i += 1
    
    return result

print(morganAndString("JACK","DANIEL"))
print(morganAndString("AAA","AAAA"))
print(morganAndString("ABA",""))
print(morganAndString("",""))




