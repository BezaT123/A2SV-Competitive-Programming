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

def multiplication(a,b):
    x=str(a)
    y=str(b)
    sum=[]
    carry=0
    product=0
    max_length = len(x) if len(x)>len(y) else len(y)
    if max_length==len(x):
        zeros=max_length-len(y)
        y=("0"*zeros)+y
    else:
        zeros=max_length-len(x)
        x=("0"*zeros)+x       
    # print(max_length)
    shift_zero=0
    for i in range(max_length-1,-1,-1):
        result=""
        for j in range(max_length-1,-1,-1):
            product= int(y[i]) * int(x[j]) + carry
            if product>=10 and j!=0:
                carry = product//10
                product= product%10        
            else:
                carry=0
            result=str(product)+result
        result=result+("0"*shift_zero)
        sum.append(int(result))
        shift_zero+=1
    print(summation_of_list(sum))

def summation_of_list(list):
    len(list)
    sum=0
    for i in list:
        sum=summation(i,sum)
    return sum




multiplication(123,1232321314)