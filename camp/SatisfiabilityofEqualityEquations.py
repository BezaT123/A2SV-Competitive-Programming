class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        leader = [x for x in range(26)]
        size  = [0] * 26
        
        def find(a):
            if leader[a] == a:
                return a
            leader[a] = find(leader[a])
            
            return leader[a]
        
        def union(a,b):
            a_lead = find(a)
            b_lead = find(b) 
            if size[a_lead] > size[b_lead]:
                leader[b_lead] = a_lead
                size[a_lead] += size[b_lead]
            else:
                leader[a_lead] = b_lead
                size[b_lead] += size[a_lead]


            
        
        for i in equations:
            if i[1] == '=':
                union(ord(i[0])- ord('a') , ord(i[3]) - ord('a'))
            
        for i in equations:
            if i[1] == '!' and find(ord(i[0]) - ord('a')) == find(ord(i[3]) - ord('a')):
                return False
        return True
