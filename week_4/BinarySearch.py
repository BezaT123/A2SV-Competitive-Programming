class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.findTarget(nums,target,0,len(nums) - 1)
        
    def findTarget(self,n, s, start, end):
        if start >= end:
            if n[start] == s:
                return start
            return -1
        mid = start + (end - start)//2
        if n[mid] == s:
            return mid
        if n[mid] > s:
            return self.findTarget(n, s, start, mid - 1)
        if n[mid] < s:
            return self.findTarget(n, s, mid + 1, end)
        
        # return -1