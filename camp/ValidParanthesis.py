class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for i in s:
            if self.isOpenTerm(i):
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                
                if not self.matches(stack.pop(), i):
                    return False
                
        return True if len(stack) == 0 else False
    
    def isOpenTerm(self, i):
        if i == "(" or i =="{" or i == "[":
            return True
        return False
    
    
    def matches(self, openTerm, closeTerm):
        for i in ["()","{}","[]"]:
            if i[0] == openTerm and i[1] == closeTerm:
                return True
            
        return False
