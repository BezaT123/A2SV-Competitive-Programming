from typing import List


class Solution:
    def minOperations(self, logs: List[str]) -> int:
        level = 0
        
        for i in range(len(logs)):
            # create directory
            if logs[i][0] != ".":
                level += 1
                
            # go back to the parent
            elif logs[i][1] != "/":
                if level > 0:
                    level -= 1
            
        return level