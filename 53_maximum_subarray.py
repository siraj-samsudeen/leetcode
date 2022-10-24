# Maximum Subarray - LeetCode
# https://leetcode.com/problems/maximum-subarray/
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum_max = sum_running = nums[0]
        for num in nums[1:]:
            # discard negative carry-overs as they can't contribute to sum
            if sum_running < 0:
                sum_running = 0
            sum_running += num
            sum_max = max(sum_max, sum_running)
        return sum_max
        