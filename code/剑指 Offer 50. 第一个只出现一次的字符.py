"""
剑指 Offer 50. 第一个只出现一次的字符
在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。 s 只包含小写字母。

示例 1:

输入：s = "abaccdeff"
输出：'b'
示例 2:

输入：s = ""
输出：' '
"""
""" 题解
遍历数组，字典保存字符是否出现一次，出现一次为True，多次为False；然后遍历字典(python3.6默认有序)，返回第一个出现一次的字符。
"""


class Solution:
    def firstUniqChar(self, s: str) -> str:
        d = {}
        for c in s:
            d[c] = not c in d
        for k, v in d.items():
            if v:
                return k
        return ' '
