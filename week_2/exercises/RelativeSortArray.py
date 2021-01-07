from typing import List

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        new_arr = []
        count_arr = [0] * len(arr2)
        end_arr = []
        for i in range(len(arr1)):
            found = False
            for j in range(len(arr2)):
                if arr1[i] == arr2[j]:
                    
                    count_arr[j] += 1
                    found = True
                    break
            if not found:
                end_arr.append(arr1[i])
                index = len(end_arr)-1
                for k in range(index-1,-1,-1):
                    if end_arr[index] < end_arr[k]:
                        end_arr[k] , end_arr[index] = end_arr[index] , end_arr[k]
                        index -= 1    
        for i in range(len(count_arr)):
            for j in range(count_arr[i]):
                new_arr.append(arr2[i])
         
        return new_arr + end_arr