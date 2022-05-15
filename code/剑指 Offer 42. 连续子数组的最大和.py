"""
剑指 Offer 42. 连续子数组的最大和
输入一个整型数组，数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。

要求时间复杂度为O(n)。
示例1:

输入: nums = [-2,1,-3,4,-1,2,1,-5,4]
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
"""
""" 前缀和解法
前缀和-当前元素之前的最小前缀和
"""


class Solution:
    def maxSubArray(self, nums) -> int:
        f = [0] * (len(nums)+1)
        nums = [0] + nums

        for i in range(len(nums)):
            f[i] = f[i-1] + nums[i]

        _min = 0
        res = float('-inf')
        for i in range(1, len(nums)):
            if f[i] - _min > res:
                res = f[i] - _min
            if f[i] < _min:
                _min = f[i]
        return res


nums = [-2,1,-3,4,-1,2,1,-5,4]
solution = Solution()
print(solution.maxSubArray(nums))

""" DP解法
①状态表达 f[i] 当前子数组的最大和。
②状态转移 f[i] = max(f[i-1]+arr[i], arr[i]) (集合中只有取与不取两个状态)。
"""


class Solution:
    def maxSubArray(self, nums) -> int:
        nums = [0] + nums
        n = len(nums)
        f = [float('-inf')] * n
        for i in range(1, n):
            f[i] = max(nums[i], f[i-1]+nums[i])
        return max(f)
