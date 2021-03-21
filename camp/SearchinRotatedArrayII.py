class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # for i in nums:
        #     if i == target:
        #         return True
        # return False
        return self.searchBS(nums, 0, len(nums) - 1, target)
    
    def searchBS(self, nums, start, end, target):
        if start >= end:
            if target == nums[start]:
                return True
            return False
        if nums[end] > nums[start]:
            # sorted, not rotated
            if nums[start] <= target <= nums[end]:
                mid = start + (end - start)//2
                if target == nums[mid]:
                    return True
                if target < nums[mid]:
                    return self.searchBS(nums, start, mid - 1, target)
                else:
                    return self.searchBS(nums, mid + 1, end , target)
            return False
        
        else:
            mid = start + (end - start)//2
            if target == nums[mid]:
                    return True
            return self.searchBS(nums, start, mid -1,target) or self.searchBS(nums, mid + 1, end, target)
