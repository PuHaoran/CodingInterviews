"""
剑指 Offer 65. 不用加减乘除做加法
写一个函数，求两个整数之和，要求在函数体内不得使用 “+”、“-”、“*”、“/” 四则运算符号。



示例:

输入: a = 1, b = 1
输出: 2
"""
""" 题解
二进制模拟加法，得到进位和不考虑进位的加和，然后继续加进位，直至进位为0；不考虑进位的加和可以用a^b表示，进位可以用a&b<<1表示。
a=3, b=7
 0 0 1 1
 0 1 1 1
----------
 0 1 0 0    carry:0 1 1 0
 0 1 1 0
----------
 0 0 1 0    carry:1 0 0 0
 1 0 0 0
----------
 1 0 1 0    carry:0 0 0 0
"""


class Solution:
    def add(self, a: int, b: int) -> int:
        x = 0xffffffff
        a, b = a & x, b & x
        while b != 0:
            a, b = (a ^ b), (a & b) << 1 & x
        return a if a <= 0x7fffffff else ~(a ^ x)
        # while b != 0:
        #     carry = (a & b) << 1
        #     a ^= b
        #     b = carry
        #
        # return a


solution = Solution()
print(solution.add(1, 2))
