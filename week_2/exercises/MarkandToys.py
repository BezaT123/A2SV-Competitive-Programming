def maximumToys(arr, k):
    # for i in range(len(arr)):
    #     min = arr[i]
    #     min_index = i
    #     for j in range(i+1,len(arr)):
    #         if arr[j] < min:
    #             min = arr[j]
    #             min_index = j
    #     arr[i],arr[min_index] = min,arr[i]
    arr.sort() 
    sum=0
    for i in range(len(arr)):
        sum += arr[i]
        if sum >= k:
            return i