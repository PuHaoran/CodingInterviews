"""
剑指 Offer 53 - I. 在排序数组中查找数字 I
统计一个数字在排序数组中出现的次数。



示例 1:

输入: nums = [5,7,7,8,8,10], target = 8
输出: 2
示例 2:

输入: nums = [5,7,7,8,8,10], target = 6
输出: 0
"""
""" 题解
二分。找最左端索引和最右端索引，然后二者相减+1即为出现次数；单调数组中找一个区间，本质是找右区间端点和左区间端点。
"""


class Solution:
    def search(self, nums, target: int) -> int:
        if len(nums) == 0:
            return 0

        def lbs(l, r, target):
            if l >= r:
                if nums[l] == target:
                    return l
                else:
                    return None

            mid = (l + r) // 2
            if nums[mid] >= target:
                r = mid
            else:
                l = mid + 1
            return lbs(l, r, target)

        def rbs(l, r, target):
            if l >= r:
                if nums[l] == target:
                    return l
                else:
                    return None
            mid = (l + r + 1) // 2
            if nums[mid] <= target:
                l = mid
            else:
                r = mid - 1
            return rbs(l, r, target)

        l, r = lbs(0, len(nums) - 1, target), rbs(0, len(nums) - 1, target)
        if l is None:
            return 0
        return r - l + 1


nums = [5, 7, 7, 8, 8, 10]
target = 10
solution = Solution()
print(solution.search(nums, target))
