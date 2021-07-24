def sockMerchant(n, ar):
    # Write your code here
    # sort nlogn
    # i, count = 0
    # iterate until i and i+1 <= n-1:
        #check if ar[i] and ar[i+1] are the same:
            # count += 1
            # move i, i+1 by 2
        # else:
            # move i, i+1 by 1
    # return count

    ar.sort()
    count = 0
    i = 0
    while i+1 <= n - 1:
        if ar[i] == ar[i+1]:
            count += 1
            i += 2
        else:
            i += 1
    return count

