from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        i = 0
        j = len(height) - 1
        max = (min(height[i], height[j]), j - i)
        while i < j:
            current = (min(height[i], height[j]), j - i)
            if current[0] * current[1] > max[0] * max[1]: 
                max = current
            
            if height[i] > height[j]:
                    j -= 1
            else:
                    i += 1
           
        
        return max[0] * max[1]