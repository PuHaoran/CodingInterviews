"""
剑指 Offer 21. 调整数组顺序使奇数位于偶数前面
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数在数组的前半部分，所有偶数在数组的后半部分。

示例：

输入：nums =[1,2,3,4]
输出：[1,3,2,4]
注：[3,1,2,4] 也是正确的答案之一。
"""
""" 题解
前后双指针，后指针找到一个奇数，前指针找到一个偶数，i<j则交换二者位置。（PS:快速排序使用了相同的技巧。）
"""


class Solution:
    def exchange(self, nums):
        i, j = -1, len(nums)
        while i < j:
            while 1:
                i += 1
                if i >= j or not nums[i] & 1:
                    break
            while 1:
                j -= 1
                if j <= i or nums[j] & 1:
                    break
            if i < j:
                nums[i], nums[j] = nums[j], nums[i]
        return nums


nums = []
solution = Solution()
print(solution.exchange(nums))
