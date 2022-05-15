"""
剑指 Offer 59 - I. 滑动窗口的最大值
给定一个数组 nums 和滑动窗口的大小 k，请找出所有滑动窗口里的最大值。

示例:

输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
输出: [3,3,5,5,6,7]
解释:

  滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
"""
""" 题解
维持一个单调递减的双端队列，每次遍历时，去掉队列中超出滑动窗口的元素，并保持队列单调递减。
"""


class Solution:
    def maxSlidingWindow(self, nums, k: int):
        from collections import deque
        q = deque()
        res = []
        for i in range(len(nums)):
            if len(q) and q[0] < i-k+1:
                q.popleft()
            while len(q) and nums[i] > nums[q[-1]]:
                q.pop()
            q.append(i)
            if i >= k-1:
                res.append(nums[q[0]])
        return res


nums = [1,3,-1,-3,5,3,6,7]
k = 3
solution = Solution()
print(solution.maxSlidingWindow(nums, k))
