class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        # heapq.heapify(stones)
        h = []
        for i in stones:
            heapq.heappush(h, -1*i)
        
        while h:
            if len(h) == 1:
                return -1 * h[0]
            x = -1 * heapq.heappop(h)
            y = -1 * heapq.heappop(h)
            
            if x != y:
                heapq.heappush(h, abs(x-y) * -1)
            
        return 0