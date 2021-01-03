def repeatedString(s, n):
    count=0
    false_case = False
    if len(s)<1 or len(s)>100:
        false_case=True
    if n < 1 or n > 10**12:
        false_case=True
        
    if not false_case:
        index_array=[]
        count=0
        for i in range(0,len(s)):
            if s[i]=='a':
                index_array.append(i)
        q , r = n // len(s) , n % len(s)
        count = count + q* len(index_array)
        
        for i in index_array:
            if i < r:
                count+=1
        return count