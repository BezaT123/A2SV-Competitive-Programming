class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        left = 0
        max_repeat = 0
        max_length = 0
        
        for right in range(len(s)):
            right_char = s[right]
            if right_char not in freq:
                freq[right_char] = 0
            freq[right_char] += 1
                
            max_repeat = max(max_repeat, freq[right_char])
            
            if (right - left + 1) - max_repeat > k:
                left_char = s[left]
                freq[left_char] -= 1
                left += 1
            max_length = max(max_length, right - left + 1)
            
        return max_length
