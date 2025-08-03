class Solution:
    def splitArray(self, nums: list[int], m: int) -> int:
        def canSplit(max_sum_allowed):
            current_sum = 0
            splits = 1
            for num in nums:
                if current_sum + num > max_sum_allowed:
                    splits += 1
                    current_sum = num
                    if splits > m:
                        return False
                else:
                    current_sum += num
            return True
        left, right = max(nums), sum(nums)
        while left < right:
            mid = (left + right) // 2
            if canSplit(mid):
                right = mid
            else:
                left = mid + 1
        return left

