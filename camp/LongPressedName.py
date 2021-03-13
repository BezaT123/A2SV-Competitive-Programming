class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        name_i = 0
        
        for i in range(len(typed)):
            if name_i + 1 < len(name) and name[name_i + 1] == typed[i]:
                    name_i += 1
            elif name[name_i] == typed[i]:
                continue
            else:
                return False
            
        return True
        
# print(Solution().isLongPressedName("saeed", "ssaaeeddd"))
# print(Solution().isLongPressedName("a", "b"))
# print(Solution().isLongPressedName("alex", "alex"))

print(ord('A'),ord('B'))