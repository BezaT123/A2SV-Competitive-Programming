class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        left , right = 0,0
        visited = set()
        max_count = 0
        
        while right < len(s):
            if s[right] in visited:
                if max_count < len(visited):
                    max_count = len(visited)
                visited.remove(s[left])
                left += 1
            else:
                visited.add(s[right])
                right +=1
        if max_count < len(visited):
            max_count = len(visited)
        return max_count
            
        
        
        
        
