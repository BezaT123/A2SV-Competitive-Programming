class Solution:
    def counting_sort(self, arr):
        counting_list = [0] * 26
        new_list =[]
        # from 97 to 122
        for i in arr:
            index = ord(i) - 97
            counting_list[index] = counting_list[index] +1
        for i in range (0, len(counting_list)):
            if i == 0:
                continue
            for j in range(counting_list[i]):
                new_list.append(chr(i+97))
            
        return new_list
        
        
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_arr =[]
        t_arr =[]
        for i in s:
            s_arr.append(i)
        for i in t:
            t_arr.append(i)
        s_arr = self.counting_sort(s_arr)
        t_arr = self.counting_sort(t_arr)

        if s_arr == t_arr:
            return True
        return False
