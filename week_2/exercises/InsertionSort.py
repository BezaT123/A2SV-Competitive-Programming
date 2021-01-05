def insertion_sort(arr):
    sorted_list_index = 0
    i=1
    while i < len(arr):    
        for j in range(sorted_list_index,-1,-1):
            if arr[i] < arr[j]:
                arr[j],arr[i] = arr[i], arr[j]
                i-=1
        sorted_list_index +=1
        i = sorted_list_index+1
    print(arr)

insertion_sort([11,-2,2,6,12,3,4,2,0,1])