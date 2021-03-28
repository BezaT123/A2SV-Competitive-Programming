class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        min_heap = []
        for i in A:
            heapq.heappush(min_heap, i)
        # print(min_heap)
        for i in range(K):
            x = heapq.heappop(min_heap)
            heapq.heappush(min_heap,-1 * x)
        
        largest_sum = 0
        for i in min_heap:
            largest_sum += i
        return largest_sum
