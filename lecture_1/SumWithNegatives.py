def summation(a,b):
    x=str(a)
    y=str(b)
    sum=0
    carry=0
    result=""
    max_length = len(x) if len(x)>len(y) else len(y)
    if max_length==len(x):
        zeros=max_length-len(y)
        y=("0"*zeros)+y
    else:
        zeros=max_length-len(x)
        x=("0"*zeros)+x       
    # print(max_length)
    for i in range(max_length-1,-1,-1):
        sum = int(x[i])+int(y[i])+carry
        if sum>=10 and i!=0:
            sum= sum%10
            carry =1
        else:
            carry=0
        result=str(sum)+result
    return int(result)

def summation_with_negatives(a,b):
    # negative = False
    x= abs(a)
    y= abs(b)

    bigger_number = a if x > y else b
    smaller_number = a if x < y else b
    if a>0 and b>0:
        return summation(a,b)
    if a < 0 and b < 0:
        return -1 * summation(x,y)
    elif bigger_number < 0 :
        return -1 * substraction(abs(bigger_number),abs(smaller_number)) 
    elif bigger_number > 0 :
        return substraction(abs(bigger_number),abs(smaller_number))

def substraction(a,b):
    x=str(a)
    y=str(b)
    difference=0
    result=""
    max_length = len(x) if len(x)>len(y) else len(y)
    if max_length==len(x):
        zeros=max_length-len(y)
        y=("0"*zeros)+y
    else:
        zeros=max_length-len(x)
        x=("0"*zeros)+x       

    for i in range(max_length-1,-1,-1):
        if int(x[i]) < int(y[i]):
            changed=int(x[i-1])-1
            x=x[:i-1]+ str(changed) + x[i]
            difference = int(x[i])+10 - int(y[i])
        else:
            difference = int(x[i]) - int(y[i])
        
        result = str(difference) + result
    return int(result)

print(summation_with_negatives(1236,6))