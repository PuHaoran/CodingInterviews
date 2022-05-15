"""
剑指 Offer 10- I. 斐波那契数列
写一个函数，输入 n ，求斐波那契（Fibonacci）数列的第 n 项（即 F(N)）。斐波那契数列的定义如下：

F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), 其中 N > 1.
斐波那契数列由 0 和 1 开始，之后的斐波那契数就是由之前的两数相加而得出。

答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。



示例 1：

输入：n = 2
输出：1
示例 2：

输入：n = 5
输出：5
"""
""" 题解
0 1 2 3 4 5 6
0 1 1 2 3 5 8
①状态表达。f(i)为前f(i-1)和f(i-2)之和。
②状态转移。f(n) = f(n-1)+f(n-2)。


输入：n = 2
输出：1
示例 2：

输入：n = 5
输出：5
"""


# 方法一：递归
class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.fib(n-1) + self.fib(n-2)


# 方法二：递推
class Solution:
    def fib(self, n: int):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        a, b = 0, 1
        for i in range(2, n+1):
            t = a+b
            a = b
            b = t
        return t % 1000000007


solution = Solution()
print(solution.fib(6))