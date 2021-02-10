from typing import List


class Solution:
    def sortArray(self, list: List[int]) -> List[int]:
        if len(list) == 1:
            return list
        middle = (len(list) - 1) // 2
        left = self.sortArray(list[:middle+1])
        right = self.sortArray(list[middle+1:])
        return self.mergingOfArrays(left,right)
        
    def mergingOfArrays(self,s,t):
        i = j = 0
        arr =[]
        while i != len(s) or j != len(t):
            if i == len(s):
                arr.append(t[j])
                j += 1
                continue
            if j == len(t):
                arr.append(s[i])
                i += 1
                continue

            if s[i] <= t[j]:
                arr.append(s[i])
                i += 1
            elif t[j] < s[i]:
                arr.append(t[j])
                j += 1
        return arr
