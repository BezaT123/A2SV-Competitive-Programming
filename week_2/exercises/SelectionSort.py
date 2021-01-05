def selection_sort(arr):
    
    for i in range(0, len(arr)):
        min = arr[i]
        min_index = i
        for j in range(i+1,len(arr)):
            if arr[j] < min:
                min = arr[j]
                min_index = j
        arr[i],arr[min_index] = min,arr[i]
    print(arr)

selection_sort([12,3,4,2,0,3,1])
