def bubble_sort(arr):
    # max = 0
    sorted = True
    while True:
        swapped = False
        for i in range(0,len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i],arr[i+1] = arr[i+1], arr[i]
                swapped = True
        if swapped == False:
            break
    print(arr)   
        
bubble_sort([12,36,16,4,0,2,1])