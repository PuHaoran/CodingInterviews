"""
剑指 Offer 53 - II. 0～n-1中缺失的数字
一个长度为n-1的递增排序数组中的所有数字都是唯一的，并且每个数字都在范围0～n-1之内。在范围0～n-1内的n个数字中有且只有一个数字不在该数组中，请找出这个数字。



示例 1:

输入: [0,1,3]
输出: 2
示例2:

输入: [0,1,2,3,4,5,6,7,9]
输出: 8
"""
""" 题解
二分。本质是寻找区间左端点（左边第一个索引与值不相等的索引）。
"""


class Solution:
    def missingNumber(self, nums) -> int:
        def bs(l, r):
            if l >= r:
                if l == nums[-1]:
                    return l+1
                return l
            mid = (l+r)//2
            if nums[mid] != mid:
                r = mid
            else:
                l = mid+1
            return bs(l, r)
        return bs(0, len(nums)-1)


nums = [0,1,2]
solution = Solution()
print(solution.missingNumber(nums))
