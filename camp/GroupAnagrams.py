class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq = {}
        result = []
        
        for i in strs:
            count_tuple = self.createCountTuple(i)
            if count_tuple in freq:
                freq[count_tuple].append(i)
            else:
                freq[count_tuple] = [i]
                
        # print(freq)
        
        for i in freq:
            result.append(freq[i])
            
        # print(result)
        return result
        
        
    def createCountTuple(self, word):
        count_array = [0] * 26
        
        for i in word:
            count_array[ord(i) - 97] += 1
            
        # print(count_array)
        
        return tuple(count_array)
            
