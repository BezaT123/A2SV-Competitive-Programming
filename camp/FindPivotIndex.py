class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sums, right_sums = [], []
        prev_sum = 0
        for i in range(len(nums)):
            if i - 1 >= 0:
                prev_sum +=nums[i - 1]
            # print(prev_sum)
            left_sums.append(prev_sum)
        # print(left_sums)
        
        prev_sum = 0
        for i in range(len(nums) - 1, -1, -1):
            if i + 1 < len(nums):
                prev_sum += nums[i+1]
            right_sums.append(prev_sum)
        # print(right_sums)
        
        for i in range(len(nums)):
            if left_sums[i] == right_sums[len(nums) - 1 - i]:
                return i
        return -1
    
