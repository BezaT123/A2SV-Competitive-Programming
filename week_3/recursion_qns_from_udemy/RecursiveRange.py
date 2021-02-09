def range(num):
    i = 0
    sum = 0
    while(i <= num):
        sum += i
        i+=1
    return sum
def recursiveRange(num):
    if num == 0:
        return 0
    return num + recursiveRange(num-1)
print(recursiveRange(10))