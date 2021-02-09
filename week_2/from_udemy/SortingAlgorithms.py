import math

def bubbleSort(list):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(list)-1):
            if list[i] > list[i+1]:
                temp_val = list[i+1]
                list[i+1] = list[i]
                list[i] = temp_val
                swapped = True
    return list

def selectionSort(list):
    
    for i in range(len(list) - 1):
        min_index = i
        for j in range(i+1,len(list)):
            if list[j] < list[min_index]:
                min_index = j
        temp = list[i]
        list[i] = list[min_index]
        list[min_index] = temp

    return list

def insertionSort(list):
    for i in range(len(list)):
        sLI = i
        for j in range(sLI - 1, -1, -1):
            if list[i] >= list[j]:
                break
            else:
                temp = list[i]
                list[i] = list[j]
                list[j] = temp
                i -=1
    return list

# doesn't work ... refer to the video... but it'snt the best sorting algorithm
def bucketSort(list):
    num_buckets = round(math.sqrt(len(list)))
    buckets = [[]] * num_buckets
    print(buckets)

    for i in range(len(list)):
        wc_bucket = math.ceil(list[i] * num_buckets / max(list)) 
        print(buckets[wc_bucket - 1])
        buckets[wc_bucket - 1].append(list[i])
    arr = []
    print(buckets)
    for i in range(len(buckets)):
        arr = arr + selectionSort(buckets[i])
    return arr

def mergingOfArrays(s,t):
    i = j = 0
    arr =[]
    while i != len(s) or j != len(t):
        if i == len(s):
            arr.append(t[j])
            j += 1
            continue
        if j == len(t):
            arr.append(s[i])
            i += 1
            continue
        
        if s[i] <= t[j]:
            arr.append(s[i])
            i += 1
        elif t[j] < s[i]:
            arr.append(t[j])
            j += 1
    return arr

def mergeSort(list):
    if len(list) == 1:
        return list
    middle = (len(list) - 1) // 2
    left = mergeSort(list[:middle+1])
    right = mergeSort(list[middle+1:])
    return mergingOfArrays(left,right)


# def pivoting(list):
#     if len(list) == 0:
#         return
#     print(len(list))
#     pivot_index = len(list) - 1
#     pivot = list[pivot_index]
#     left = 0
#     right = len(list) - 2
#     while True:
#         if left > right:
#             temp = list[left]
#             list[left] = list[len(list)-1]
#             list[len(list)-1] = temp
#             pivot_index = left
#             break
#         if list[left] < pivot:
#             left += 1
#             continue
#         if list[right] >= pivot:
#             right -= 1
#             continue
        
#         temp = list[left]
#         list[left] = list[right]
#         list[right] = temp
#     print(list)
#     return pivot_index

# def quickSort(list):
#     if len(list) == 1:
#         return list
#     pivot = pivoting(list)
#     quickSort(list[:pivot])
#     quickSort(list[pivot + 1:])
#     return list

def pivoting(list,left,right):
    print(len(list))
    pivot_index = right
    pivot = list[pivot_index]
    right = right -1
    while True:
        if left > right:
            temp = list[left]
            list[left] = list[len(list)-1]
            list[len(list)-1] = temp
            pivot_index = left
            break
        if list[left] < pivot:
            left += 1
            continue
        if list[right] >= pivot:
            right -= 1
            continue
        
        temp = list[left]
        list[left] = list[right]
        list[right] = temp
    print(list)
    return pivot_index

def quickSort(list,start,end):
    if start < end:
        pivot = pivoting(list,start,end)
        quickSort(list, start,pivot-1)
        quickSort(list, pivot+1, end)
    return list

print(quickSort([3,1,5,2,7,9,0,6],0,7)) 
        