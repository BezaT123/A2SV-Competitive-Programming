class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        max_length = 1
        increasing = False
        left = 0
        for i in range(len(arr) -1):
            if i == 0:
                if arr[i] > arr[i+1]:
                    increasing = False
                elif arr[i] < arr[i+1]:
                    increasing = True
                else:
                    left += 1
            else:
                if increasing and arr[i] > arr[i + 1]:
                    increasing = False
                elif not increasing and arr[i] < arr[i+1]:
                    increasing = True
                
                else:
                    print(arr[i], arr[i+1])
                    
                    max_length = max(max_length, i - left + 1)
                    left = i
                    if arr[i] == arr[i+1]:
                        left = i + 1
        max_length = max(max_length, len(arr) - 1 - left + 1)    
        return max_length
