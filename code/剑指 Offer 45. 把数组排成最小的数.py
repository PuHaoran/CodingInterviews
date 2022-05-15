"""
剑指 Offer 45. 把数组排成最小的数
输入一个非负整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。



示例 1:

输入: [10,2]
输出: "102"
示例 2:

输入: [3,30,34,5,9]
输出: "3033459"
"""
""" 题解
快排。两元素比较规则：x + y < y + x => x < y;y + x < x + y => y < x。
eg：x=10, y=20；1020 < 2010 => 10 < 20

 3 1 2 4 5
i          j
 i   j      
 2 1 3 4 5
   j i
 2 1     3 4 5
"""


class Solution:
    def minNumber(self, nums):
        nums = [str(i) for i in nums]
        def quick_sort(l, r):
            if l >= r:
                return
            i, j = l-1, r+1
            x = nums[l]
            while i < j:
                while 1:
                    i += 1
                    if nums[i] + x >= x + nums[i]:
                        break
                while 1:
                    j -= 1
                    if nums[j] + x <= x + nums[j]:
                        break
                if i < j:
                    nums[i], nums[j] = nums[j], nums[i]
            quick_sort(l, j)
            quick_sort(j+1, r)

        quick_sort(0, len(nums)-1)
        return ''.join(nums)


nums = [10,2]
solution = Solution()
solution.minNumber(nums)
