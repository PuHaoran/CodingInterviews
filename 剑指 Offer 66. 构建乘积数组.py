"""
剑指 Offer 66. 构建乘积数组
给定一个数组 A[0,1,…,n-1]，请构建一个数组 B[0,1,…,n-1]，其中 B[i] 的值是数组 A 中除了下标 i 以外的元素的积, 即 B[i]=A[0]×A[1]×…×A[i-1]×A[i+1]×…×A[n-1]。不能使用除法。



示例:

输入: [1,2,3,4,5]
输出: [120,60,40,30,24]
"""
""" 题解
每一行所有除对角线元素相乘即为乘积数组的元素。先从上到下构建下三角乘积数组，然后从下到上构建上三角乘积数组。
      a
f[0]  1 2 3 4 
f[1]  1 1 3 4
f[2]  1 2 1 4 
f[3]  1 2 3 1
"""


class Solution:
    def constructArr(self, a):
        f = [1] * len(a)
        # 下三角
        for i in range(1, len(a)):
            f[i] = f[i-1] * a[i-1]
        # 上三角
        t = 1
        for i in range(len(a)-2, -1, -1):
            t *= a[i+1]
            f[i] *= t
        return f


a = [1,2,3,4,5]
solution = Solution()
print(solution.constructArr(a))
