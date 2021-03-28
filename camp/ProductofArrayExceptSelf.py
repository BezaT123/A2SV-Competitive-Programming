class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_product = []
        right_product = []
        answer = []
        prev_product = 1
        
        for i in range(len(nums)):
            if i - 1 >= 0:
                prev_product = prev_product * nums[i - 1]
            left_product.append(prev_product)
            
        prev_product = 1
        
        for i in range(len(nums) -1, -1, -1):
            if i + 1 < len(nums):
                prev_product *= nums[i + 1]
            right_product.append(prev_product)
        
        # print(left_product, right_product)
        
        for i in range(len(nums)):
            answer.append(left_product[i] * right_product[len(nums) - i - 1])
        
        return answer
