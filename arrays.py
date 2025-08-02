class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [0] * n
        product = 1
        for i in range(n):
            left[i] = product
            product *= nums[i]
        right = [0] * n
        product = 1
        for i in range(n - 1, -1, -1):
            right[i] = product
            product *= nums[i]
        ans = [0] * n
        for i in range(n):
            ans[i] = left[i] * right[i]            
        return ans
