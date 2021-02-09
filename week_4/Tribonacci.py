class Solution:
    # def tribonacci(self, n: int) -> int:
    #     if n == 0:
    #         return 0
    #     if n == 1 or n == 2:
    #         return 1
    #     return self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        
        prev = 1
        sec_prev = 1
        third_prev = 0
        
        sum = 0
        i = 3
        
        while i <= n:
            sum = prev + sec_prev + third_prev
            third_prev = sec_prev
            sec_prev = prev
            prev = sum
            i += 1
        return sum