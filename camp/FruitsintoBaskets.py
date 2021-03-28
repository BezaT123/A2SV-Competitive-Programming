class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        freq = {}
        visited = set()
        
        left = 0
        max_length = 0
        
        for i in range(len(tree)):
            visited.add(tree[i])
            if len(visited) > 2:
                while len(visited) > 2:
                    freq[tree[left]] -= 1
                    if freq[tree[left]] == 0:
                        visited.remove(tree[left])
                    left += 1
            if tree[i] not in freq:
                freq[tree[i]] = 0
            freq[tree[i]] += 1
            max_length = max(max_length, i - left + 1)
                
        return max_length
