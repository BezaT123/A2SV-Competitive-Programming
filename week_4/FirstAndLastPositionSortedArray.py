from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result = [-1,-1]
        first_time_found = True
        
        if len(nums) == 0:
            return result
        
        if target > nums[len(nums)-1] or target < nums[0]:
            return result
        
        for i in range(len(nums)):
            if nums[i] > target:
                return result
            if nums[i] == target and first_time_found:
                result[0] = i
                first_time_found = False
            if nums[i] == target and not first_time_found:
                result[1] = i
                
        return result