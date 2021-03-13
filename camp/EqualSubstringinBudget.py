class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
#         count = 0
        
#         for i in range(len(s)):
#             print(s[i], t[i],abs(ord(s[i]) - ord(t[i])))
#             if 0 < abs(ord(s[i]) - ord(t[i])) <= maxCost:
#                 maxCost -= abs(ord(s[i]) - ord(t[i]))
#                 count += 1
#         return count     
        
#         max_count = 0
#         i = 0
#         j = 0
#         count = 0
#         cost = 0

#         while i < len(s):
#             cost += abs(ord(s[j]) - ord(t[j]))
#             if cost > maxCost:
#                 if count > max_count:
#                     max_count = count
#                 j += 1
#                 i = 0
#                 count = 0
#                 cost = 0
#                 continue
            
#             count += 1
#             i += 1
        cost_list = []
        
        for i in range(len(s)):
            cost_list.append(abs(ord(s[i]) - ord(t[i])))
        print(cost_list)
        
        max_count =0
        sum = 0
        start_i = 0 
        end_i = 0
        
#         for i in range(len(cost_list)):
#             if sum + cost_list[i] <= maxCost:
#                 sum += cost_list[i]
#             else:
#                 end_i = i
#                 break
            
#         max_count = end_i + 1
        
#         end_i += 1
        
        while end_i < len(s):
            
            while sum + cost_list[end_i] > maxCost:
                sum -= cost_list[start_i]
                start_i += 1
            sum += cost_list[end_i]
            if max_count < end_i - start_i + 1:
                max_count = end_i - start_i + 1
                
            end_i += 1
        
        return max_count

print(Solution().equalSubstring("abcde","bcdld",3))