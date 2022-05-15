"""
剑指 Offer 16. 数值的整数次方
实现 pow(x, n) ，即计算 x 的 n 次幂函数（即，xn）。不得使用库函数，同时不需要考虑大数问题。

示例 1：

输入：x = 2.00000, n = 10
输出：1024.00000
示例 2：

输入：x = 2.10000, n = 3
输出：9.26100
示例 3：

输入：x = 2.00000, n = -2
输出：0.25000
解释：2-2 = 1/22 = 1/4 = 0.25
"""
""" 题解
快速幂。分治算法，当n为偶数x^(n//2)*x^(n//2)，n为奇数x^(n//2)*x^(n//2)*x，递归求解。
①n为偶数，x->x2->x4->x8->x16->x32->x64。
②n为奇数，x->x2->x4->x8->x16->x33->x67。
"""


class Solution:
    def myPow(self, x: float, n: int) -> float:
        def quick_mul(x, n):
            """ 快速幂 """
            if n == 0:
                return 1
            y = quick_mul(x, n >> 1)
            return y * y if n % 2 == 0 else y * y * x
        return quick_mul(x, n) if n >= 0 else quick_mul(x, -n)


solution = Solution()
print(solution.myPow(0.44, -2))
