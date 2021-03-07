from typing import List
from collections import heapq


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        
        i = j = 0
        count = 0
        result = []
        h =[]
        visited = []
        
        if len(nums1) == 0 or len(nums2) == 0:
            return h
        
        heapq.heappush(h,(nums1[i] + nums2[j],[i,j]))
        visited.append([i,j])

        
        while len(h) > 0:
            s,l = heapq.heappop(h)
            i = l[0]
            j = l[1]
            result.append([nums1[i], nums2[j]])
            count += 1
            
            if count == k:
                break
                
            if i + 1 < len(nums1):
                path_i = [i+1,j]
                if path_i not in visited:
                    heapq.heappush(h,(nums1[i+1] + nums2[j],path_i))
                    visited.append(path_i)
            
            if j + 1 < len(nums2):
                path_j = [i,j+1]
                if path_j not in visited:
                    heapq.heappush(h,(nums1[i] + nums2[j+1],path_j))
                    visited.append(path_j)

        return result