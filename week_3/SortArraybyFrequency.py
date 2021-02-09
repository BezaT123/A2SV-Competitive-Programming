from typing import List


class Solution:

    def sortbyValues(self,item):
        return item[1]

    def frequencySort(self, nums: List[int]) -> List[int]:
        freq = {}
        for i in range(len(nums)):
            freq[nums[i]] = freq.get(nums[i],0) + 1
        freq = dict(sorted(freq.items(),key= self.sortbyValues))
        print(freq)

        for i in freq.values():
            

    

Solution().frequencySort([-6,0,1,1,3,2,2,2])