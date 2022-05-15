"""
剑指 Offer 20. 表示数值的字符串
请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。

数值（按顺序）可以分成以下几个部分：

若干空格
一个 小数 或者 整数
（可选）一个 'e' 或 'E' ，后面跟着一个 整数
若干空格
小数（按顺序）可以分成以下几个部分：

（可选）一个符号字符（'+' 或 '-'）
下述格式之一：
至少一位数字，后面跟着一个点 '.'
至少一位数字，后面跟着一个点 '.' ，后面再跟着至少一位数字
一个点 '.' ，后面跟着至少一位数字
整数（按顺序）可以分成以下几个部分：

（可选）一个符号字符（'+' 或 '-'）
至少一位数字
部分数值列举如下：

["+100", "5e2", "-123", "3.1416", "-1E-16", "0123"]
部分非数值列举如下：

["12e", "1a3.14", "1.2.3", "+-5", "12e+5.4"]


示例 1：

输入：s = "0"
输出：true
示例 2：

输入：s = "e"
输出：false
示例 3：

输入：s = "."
输出：false
示例 4：

输入：s = "    .1  "
输出：true
"""
""" 题解
去掉两端空格，遍历字符串，判断e、.、符号不满足条件的所有情况。
"""


class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        if not len(s):
            return False

        dot = 0
        e = 0
        e_list = ['E', 'e']
        digit_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        mark_list = ['+', '-']
        n = len(s)

        for i in range(len(s)):
            if (s[i] == '+' or s[i] == '-'):
                if (i and s[i-1] not in e_list) or i == n-1 or s[i+1] not in digit_list+['.']:
                    return False
            elif s[i] in e_list:
                if e or i == 0 or i == n-1:
                    return False
                for j in range(i+1, len(s)):
                    if s[j] not in digit_list+mark_list:
                        return False
                e += 1
            elif s[i] == '.':
                # .e3 => False
                if i == 0 and i+1<n and s[i+1] in e_list:
                    return False
                if dot or not ((i==n-1 and s[i-1] in digit_list) or (i==0 and i+1<n and s[i+1] in digit_list+e_list) or (i>0 and i<n-1 and s[i-1] in digit_list+mark_list and s[i+1] in digit_list+e_list)):
                    return False
                dot += 1
            elif s[i] not in e_list+digit_list+mark_list+['.']:
                return False

        return True


solution = Solution()
for s in ["12e", "1a3.14", "1.2.3", "+-5", "12e+5.4"]:
    print(solution.isNumber(s))
