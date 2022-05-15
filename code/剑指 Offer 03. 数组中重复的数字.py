"""
剑指 Offer 03. 数组中重复的数字
找出数组中重复的数字。


在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。

示例 1：

输入：
[2, 3, 1, 0, 2, 5, 3]
输出：2 或 3
"""
""" 题解
根据每个数字都有一个对应的索引。
若当前元素已经在对应索引上则遍历下一个元素；若当前元素不等于对应的索引，则与对应索引的元素进行交换，保证该元素在对应索引上，但若对应索引已经有一个正确的元素，那说明当前元素为重复元素。

[2, 3, 1, 0, 2, 5, 3]
输出：2 或 3
"""


class Solution:
    def findRepeatNumber(self, nums):
        i = 0
        while i < len(nums):
            t = nums[i]
            if t == i:
                i += 1
            else:
                if nums[t] == t:
                    return t
                nums[i], nums[t] = nums[t], nums[i]


arr = [2, 3, 1, 0, 2, 5, 3]
solution = Solution()
print(solution.findRepeatNumber(arr))
