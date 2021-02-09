# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        # print(isBadVersion(1))
        return self.findFirstBad(n,1,n)
    
    def findFirstBad(self, n,start, end):
        if start == end:
            return start
        mid = start + (end - start) // 2
        
        if isBadVersion(mid):
            return self.findFirstBad(n, start, mid)
        else:
            return self.findFirstBad(n, mid+1, end)
            

        