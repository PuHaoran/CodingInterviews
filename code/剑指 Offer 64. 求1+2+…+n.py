"""
剑指 Offer 64. 求1+2+…+n
求 1+2+...+n ，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。



示例 1：

输入: n = 3
输出: 6
示例 2：

输入: n = 9
输出: 45
"""
""" 题解
布尔判断作为递归终止条件。 
"""


class Solution:
    def sumNums(self, n: int) -> int:
        global res
        res = 0
        def get_sum(n):
            global res
            n and get_sum(n-1)
            res += n
            return res
        return get_sum(n)
