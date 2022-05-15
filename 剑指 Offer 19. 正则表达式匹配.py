"""
剑指 Offer 19. 正则表达式匹配
请实现一个函数用来匹配包含'. '和'*'的正则表达式。模式中的字符'.'表示任意一个字符，而'*'表示它前面的字符可以出现任意次（含0次）。在本题中，匹配是指字符串的所有字符匹配整个模式。例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但与"aa.a"和"ab*a"均不匹配。

示例 1:

输入:
s = "aa"
p = "a"
输出: false
解释: "a" 无法匹配 "aa" 整个字符串。
示例 2:

输入:
s = "aa"
p = "a*"
输出: true
解释: 因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。
"""
""" 题解
①状态表示。f(i,j)，f(i,j)是s和p是否存在一个合法方案。
②状态转移。s和p为两个串,f为状态转移方程，则
s---------------
               i
p-------------
             j
1. p[j] not '*' and i, f(i,j)=(s[i]==p[j]||p[j]=='.')&&f(i-1,j-1)
2. p[j] == '*', f(i,j)=f(i,j-2)||(f(i-1,j-2)&&s[i]==p[j-1])||(f(i-2,j-2)&&s[i]==p[j-1]&&s[i-1]==p[j-1]) ①
               f(i-1,j)=f(i-1,j-2)||(f(i-2,j-2)&&s[i-1]==p[j-1])||(f(i-3,j-2)&&s[i-1]==p[j-1]&&s[i-2]==p[j-1]) ②
=>
f(i,j)=f(i,j-2)||(f(i-1,j)&&(s[i]==p[j-1]||p[j-1]=='.'))
"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n, m = len(s), len(p)
        f = [[False]*(m+1) for _ in range(n+1)]
        s, p = ' '+s, ' '+p
        f[0][0] = True
        for i in range(n+1):
            for j in range(1, m+1):
                if j+1 <= m and p[j+1] == '*':
                    continue
                if i and p[j] != '*':
                    f[i][j] = f[i-1][j-1] and (s[i] == p[j] or p[j] == '.')
                elif p[j] == '*':
                    f[i][j] = bool(f[i][j-2] or i and f[i-1][j] and (s[i] == p[j-1] or p[j-1] == '.'))
        return f[n][m]
