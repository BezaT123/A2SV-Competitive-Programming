"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        emp_map = {}
        for i in employees:
            emp_map[i.id] = [i.importance,i.subordinates]
        # print(emp_map, emp_map[id], emp_map[id][1])
        
        return self.dfs(emp_map, id)
    
    
    
    def dfs(self, emp_map, id):
        
        employee = emp_map[id]
        imp = employee[0]
        sub = employee[1]
        
        sum = employee[0]
        
        if len(sub) != 0:
            for i in sub:
                sum += self.dfs(emp_map, i)
            
        return sum
   
