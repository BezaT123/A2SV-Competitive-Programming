def divisibleSumPairs(n, k, ar):
    false_case=False
    count=0
    if n<2 or n>100:
        false_case=True
    if k<1 or k>100:
        false_case=True
    if not false_case:
        for i in range(0,n-1):
            if ar[i]<1 or ar[i]>100:
                continue        
            for j in range(i+1,n):
                if i < j and (ar[i]+ar[j])% k == 0:
                    count+=1
        return count