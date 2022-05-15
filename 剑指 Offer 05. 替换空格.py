"""
剑指 Offer 05. 替换空格
请实现一个函数，把字符串 s 中的每个空格替换成"%20"。



示例 1：

输入：s = "We are happy."
输出："We%20are%20happy."
"""
""" 题解
法一：
利用python的语言特性可以先转化为数组，然后依次遍历进行替换。
法二：
先利用空格数量开辟空间，然后根据双指针所指的元素从后向前进行替换操作。
we are happy.
            i        j
we are happy.        .
           i        j
...
we are happy.   happy.
      i        j
we are happy.  %20happy.
     i        j
we%20are%20happy.
 ij

输入：s = "We are happy."
输出："We%20are%20happy."
"""
# 法一
# class Solution:
#     def replaceSpace(self, s: str) -> str:
#         s = list(s)
#         for i in range(len(s)):
#             if s[i] == ' ':
#                 s[i] = '%20'
#         return ''.join(s)


class Solution:
    def replaceSpace(self, s: str) -> str:
        s = list(s)
        cnt = 0
        for i in range(len(s)):
            if s[i] == ' ':
                cnt += 1
        i, j = len(s)-1, len(s)+cnt*2-1
        s += ['']*cnt*2
        while i >= 0:
            if s[i] == ' ':
                s[j] = '0'
                s[j-1] = '2'
                s[j-2] = '%'
                j -= 3
            else:
                s[j] = s[i]
                j -= 1
            i -= 1
        return ''.join(s)
