class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        arr = []
        for i in range(len(nums1)):
            found = False
            repeated = False
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    found = True    
            if found:
                for k in range(len(arr)):
                    if arr[k] == nums1[i]:
                        repeated = True
                        break
                if not repeated:
                    arr.append(nums1[i])                
        return arr