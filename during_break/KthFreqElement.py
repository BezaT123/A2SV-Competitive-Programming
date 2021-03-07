from typing import List
from collections import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myDict = {}
        # count = 0
        for i in nums:
            if i in myDict:
                myDict[i] += 1
            else:
                myDict[i] = 1
        
        print(myDict)
        h = []
        heapq.heapify(h)
        
        for key,val in myDict.items():
            if len(h) >= k:
                heapq.heappush(h, [val,key])
                heapq.heappop(h)
            else:
                heapq.heappush(h, [val,key])
        
        answer = []
        for v,k in h:
            answer.append(k)
        return answer