"""
剑指 Offer 51. 数组中的逆序对
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组，求出这个数组中的逆序对的总数。



示例 1:

输入: [7,5,6,4]
输出: 5
"""
""" 题解
归并排序过程对A、B两个有序数组进行比较，若arr[i]<=arr[j]，则i+=1，若arr[i]>arr[j]，则j+1，此时共mid-i+1个数均大于arr[j]。
  l        mid  mid+1    r
A |________|  B|_________|
    i            j
"""


class Solution:
    def reversePairs(self, nums) -> int:
        def merge_sort(l, r):
            if l >= r:
                return 0
            mid = (l+r)//2
            res = merge_sort(l, mid) + merge_sort(mid+1, r)
            i, j = l, mid+1
            temp = []
            while i <= mid and j <= r:
                if nums[i] <= nums[j]:
                    temp.append(nums[i])
                    i += 1
                else:
                    temp.append(nums[j])
                    res += mid-i+1
                    j += 1
            if i <= mid:
                temp += nums[i:mid+1]
            if j <= r:
                temp += nums[j: r]
            for i in range(len(temp)):
                nums[l+i] = temp[i]
            return res
        return merge_sort(0, len(nums)-1)


nums = [7,5,6,4]
solution = Solution()
print(solution.reversePairs(nums))
