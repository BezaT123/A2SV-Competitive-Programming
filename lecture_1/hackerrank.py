def sockMerchant(n, ar):
    matching_pairs=0
    for i in range(0,len(ar)):
        for j in range(i+1,len(ar)):
            if ar[i]==ar[j]:
                matching_pairs+=1
                ar.pop(j)
                break
    return matching_pairs

