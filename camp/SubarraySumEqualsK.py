class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        freq = {0:1}
        prefix_sum = []
        prev_sum = 0
        for i in nums:
            prev_sum += i
            prefix_sum.append(prev_sum)
        
        # print(prefix_sum)
        prev_sum = 0
        count = 0
        for i in prefix_sum:
            prev_sum = i - k
            if prev_sum in freq:
                count += freq[prev_sum]
                
            if i not in freq:
                freq[i] = 0
            freq[i] += 1
            
            
            
        return count
            
        
                
