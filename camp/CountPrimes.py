class Solution:
    def countPrimes(self, n: int) -> int:
        num_of_primes = 0
        num_list = [1] * n
        
        if n < 2:
            return 0
        
        num_list[0] = 0
        num_list[1] = 0

        
        for i in range(2, int(sqrt(n)) + 1):
            if num_list[i]:
                for k in range(i*i, n, i):
                    num_list[k] = 0
                    
        return sum(num_list)
        
