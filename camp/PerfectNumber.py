class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        result = 1
        i = 2
        
        while i <= sqrt(num):
            if num % i == 0:
                result = result + i + num // i
            i += 1
        if result == num and result != 1:
            return True
        return False
