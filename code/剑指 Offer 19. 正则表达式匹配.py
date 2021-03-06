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
①状态表示。f(i,j)表示s[1...i]与p[1...j]的所有匹配方案是否有一成立。
②状态转移，求f(i,j)。 
    p[j] != '*' 
        f(i, j) = (s[i] == p[j] or p[j] == '.') and f(i-1, j-1)
    p[j] == '*' 
p[j] == '*'情况的图示
                   i
o    o    o    o   o
o    o    o    o   *
         j-2  j-1  j
注意：*和*前面一个数应视为一个整体，当*代表0个数时，其前面一个数也没有意义。
*表示0个，f(i, j-2)
*表示1个，f(i-1,j-2) and s[i] == p[j-1]
*表示2个，f(i-2,j-2) and s[i] == p[j-1] and s[i-1] == p[j-1]
=> 
f(i,j) = f(i,j-2) or (f(i-1,j-2) and s[i] == p[j-1]) or (f(i-2,j-2) and s[i] == p[j-1] and s[i-1] == p[j-1]) ①
f(i-1,j) = f(i-1,j-2) or (f(i-2,j-2) and s[i-1] == p[j-1]) or (f(i-2,j-2) and s[i-1] == p[j-1] and s[i-2] == p[j-1]) ②
由①与②得
f(i,j)=f(i,j-2) or (i and (f(i-1,j) and s[i] == p[j-1])
"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        f = [[0]*(n+1) for _ in range(m+1)]
        s, p = ' ' + s, ' ' + p
        f[0][0] = 1
        for i in range(0, m+1): # s为空，p不为空也可能匹配，故s从0开始
            for j in range(1, n+1): # s不为空，p为空一定不匹配，故从1开始
                # *和其前面的数视为一个整体考虑，当遍历到*前面的数则直接跳过
                if j+1 <= n and p[j+1] == '*':
                    continue
                if i and p[j] != '*':
                    f[i][j] = (s[i] == p[j] or p[j] == '.') and f[i-1][j-1]
                elif p[j] == '*':
                    f[i][j] = f[i][j-2] or (i and f[i-1][j] and (s[i] == p[j-1] or p[j-1] == '.'))
        return bool(f[m][n])
