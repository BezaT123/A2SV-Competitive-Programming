class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        if arr[start] == 0:
            return True
        visted = set([start])
        queue = deque()
        queue.append(start)
        direction = [-1,1]
        while queue:
            popped = queue.popleft()
            
            if arr[popped] == 0:
                return True
            
            for i in direction:
                path = popped + arr[popped] * i


                if  0 <= path < len(arr) and path not in visted:
                    queue.append(path)
                    visted.add(path)


        return False
