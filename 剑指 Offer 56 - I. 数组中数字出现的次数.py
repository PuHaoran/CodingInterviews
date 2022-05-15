"""
剑指 Offer 56 - I. 数组中数字出现的次数
一个整型数组 nums 里除两个数字之外，其他数字都出现了两次。请写程序找出这两个只出现一次的数字。要求时间复杂度是O(n)，空间复杂度是O(1)。



示例 1：

输入：nums = [4,1,4,6]
输出：[1,6] 或 [6,1]
示例 2：

输入：nums = [1,2,10,4,1,4,3,3]
输出：[2,10] 或 [10,2]
"""
""" 题解
位运算。先将数组的每个元素逐个进行异或，然后对结果取lowbit（不相等的两个元素可通过与lowbit进行&操作区分）；
然后再次遍历数组并根据&的结果进行分组，分组的元素异或后的结果就是目标元素。

求x的二进制数最低位1的位置lowbit为何可以用x & -x表示？
计算机采用二进制的补码进行数学运算，其中正数的补码是原码，负数的补码是原码取反+1，故
7 & -7 =》 000111 & 111001 =》 000001 =》1。
4 & -4 =》 000100 & 111100 =》 000100 =》4。
"""


class Solution:
    def singleNumbers(self, nums):
        xy = 0
        for num in nums:
            xy ^= num
        lowbit = xy & -xy
        a, b = 0, 0
        for num in nums:
            if num & lowbit:
                a ^= num
            else:
                b ^= num
        return [a, b]


nums = [4,1,4,6]
solution = Solution()
print(solution.singleNumbers(nums))
