"""
剑指 Offer 11. 旋转数组的最小数字
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。

给你一个可能存在 重复 元素值的数组 numbers ，它原来是一个升序排列的数组，并按上述情形进行了一次旋转。请返回旋转数组的最小元素。例如，数组 [3,4,5,1,2] 为 [1,2,3,4,5] 的一次旋转，该数组的最小值为1。

示例 1：

输入：[3,4,5,1,2]
输出：1
示例 2：

输入：[2,2,2,0,1]
输出：0
"""
""" 解析
左边数组一定小于等于右边数组，故我们可以通过二分来缩减筛选范围。
arr[mid] > arr[r]  l=mid+1
arr[mid] < arr[r] r=mid
arr[mid] == arr[r] r=r-1

输入：[3,4,5,1,2]
输出：1
示例 2：

输入：[2,2,2,0,1]
输出：0
"""


class Solution:
    def minArray(self, numbers) -> int:
        def binary_search(numbers, l, r):
            if l >= r:
                return numbers[l]
            mid = (l + r) // 2
            if numbers[mid] < numbers[r]:
                r = mid
            elif numbers[mid] == numbers[r]:
                r -= 1
            else:
                l = mid + 1
            return binary_search(numbers, l, r)
        return binary_search(numbers, 0, len(numbers)-1)


numbers = [3,4,5,1,2]
solution = Solution()
print(solution.minArray(numbers))
