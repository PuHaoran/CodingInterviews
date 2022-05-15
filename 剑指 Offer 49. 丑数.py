"""
剑指 Offer 49. 丑数
我们把只包含质因子 2、3 和 5 的数称作丑数（Ugly Number）。求按从小到大的顺序的第 n 个丑数。



示例:

输入: n = 10
输出: 12
解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。
说明:

1 是丑数。
n 不超过1690。
"""
""" 题解
DP+三指针
①状态表示 f(i)第i个丑数对应的数字。
②状态转移 f(i)=min(f(a)*2,f(b)*3,f(c)*5)，其中a、b、c是从头开始移动的三个指针，abc中一定存在一个或多个恰好大于f[i-1]的数。
"""


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        a, b, c = 0, 0, 0
        f = [0] * n
        f[0] = 1
        i = 1
        while i < n:
            _min = min(f[a]*2, f[b]*3, f[c]*5)
            if _min == f[a]*2:
                a += 1
            if _min == f[b]*3:
                b += 1
            if _min == f[c]*5:
                c += 1
            f[i] = _min
            i += 1
        return f[n-1]


solution = Solution()
print(solution.nthUglyNumber(10))
