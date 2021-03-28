class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        left = 0
        
        for i in t:
            if left < len(s) and i == s[left]:
                left += 1
        
        if left <= len(s) - 1:
            return False
        return True
