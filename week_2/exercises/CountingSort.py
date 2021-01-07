def counting_sort(arr):
    max = arr[0]
    for i in range(1,len(arr)):
        # max = max(max,arr[i])
        if arr[i] > max:
            max= arr[i]
        
    
    count_arr = [0] * (max+1)
    print(max,count_arr)
    for i in range(0,len(arr)):
        index = arr[i]
        count_arr[index] = count_arr[index]+1
    # print(count_arr)

    sorted_arr =[]
    for i in range(0,len(count_arr)):
        if count_arr[i] == 0:
            continue
        for j in range(0,count_arr[i]):
            sorted_arr.append(i)
    return sorted_arr

print(counting_sort([0, 2,5,1,0,4]))