class Solution:
    def trailingZeroes(self, n: int) -> int:
        i = 5
        result = 0
        while i <= n:
            result += n//i
            i *= 5
        return result
