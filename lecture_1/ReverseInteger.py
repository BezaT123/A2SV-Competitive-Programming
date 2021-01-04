class Solution:
    def reverse(self, x: int) -> int:
        y= abs(x)
        result=0
        if x < -2 ** 31 or x > (2 ** 31) - 1:
            return 0
        while y!=0:
            
            digit = y % 10
            result = result *10 +digit
            y=y//10
            if result < -2 ** 31 or result > (2 ** 31) - 1:
                return 0
        if x<0:
            result*=-1
        return result