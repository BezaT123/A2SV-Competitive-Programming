class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        memo = {}
        return self.countPalindromeSubseq(s, 0, len(s) - 1, memo)
    
    def countPalindromeSubseq(self, s, left, right, memo):
        
        if (left, right) in memo:
            return memo[(left,right)]
        
        if left == right:
            memo[(left, right)] = 1
            return memo[(left, right)]
            
        if left > right:
            return 0
        
        if s[left] == s[right]:
            memo[(left, right)] = 2 + self.countPalindromeSubseq(s, left + 1, right - 1, memo)
            return memo[(left, right)]
        else:
            memo[(left, right)] = max(self.countPalindromeSubseq(s, left + 1, right, memo), self.countPalindromeSubseq(s, left, right - 1, memo))
            return memo[(left, right)]

