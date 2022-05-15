"""
剑指 Offer 15. 二进制中1的个数
编写一个函数，输入是一个无符号整数（以二进制串的形式），返回其二进制表达式中数字位数为 '1' 的个数（也被称为 汉明重量).）。

示例 1：

输入：n = 11 (控制台输入 00000000000000000000000000001011)
输出：3
解释：输入的二进制串 00000000000000000000000000001011 中，共有三位为 '1'。
"""
""" 题解
位运算
求n二进制最后一位数字，n & 1；消除最低位的1，n&(n-1)。
11 => 1011 => 1011 & 1010 => 1010
10 => 1010 => 1010 & 1001 => 1000
"""


class Solution:
    def hammingWeight(self, n: int):
        res = 0
        while n:
            res += n & 1
            n = n >> 1
        return res


solution = Solution()
print(solution.hammingWeight(128))


class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            res += 1
            n = n & n-1
        return res
