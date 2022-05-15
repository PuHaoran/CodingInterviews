"""
剑指 Offer 56 - II. 数组中数字出现的次数 II
在一个数组 nums 中除一个数字只出现一次之外，其他数字都出现了三次。请找出那个只出现一次的数字。



示例 1：

输入：nums = [3,4,3,3]
输出：4
示例 2：

输入：nums = [9,1,7,9,7,9,7]
输出：1
"""
""" 题解
利用n >> k & 1，求n的第k位二进制数。两层循环，外层遍历共31位的二进制数，内层遍历所有元素，所有元素k位求和%3得到多余的数在k位上的数字。
"""


class Solution:
    def singleNumber(self, nums) -> int:
        res = 0
        for i in range(31, -1, -1):
            t = 0
            for num in nums:
                t += num >> i & 1
            res = res*2 + t%3
        return res


nums =  [9,1,7,9,7,9,7]
solution = Solution()
print(solution.singleNumber(nums))
