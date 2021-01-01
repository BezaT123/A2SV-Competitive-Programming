from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l=[]
        for i in range(0,len(nums)):
            # x=target-nums[i]
            # if x in nums and x!=nums[i]:
            #     l.append(i)
            #     index=nums.index(x)
            #     l.append(index)
            #     break
            for j in range(i+1, len(nums)):
                if nums[j]+nums[i] == target:
                    l.append(i)
                    l.append(j)

        return l

print(Solution().twoSum(nums=[2,7,11,15],target=9))