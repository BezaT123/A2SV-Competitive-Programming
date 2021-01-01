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
    print(result)