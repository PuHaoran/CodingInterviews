"""
剑指 Offer 38. 字符串的排列
输入一个字符串，打印出该字符串中字符的所有排列。



你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。



示例:

输入：s = "abc"
输出：["abc","acb","bac","bca","cab","cba"]
"""
"""
输入：s = "abc"
输出：["abc","acb","bac","bca","cab","cba"]
"""
""" 题解
DFS，使用数组mark标记走过的路径，函数传递u作为终止条件。 
    o
    /\ \
    a b c
    /\ ...
    b c
    / /
    c b
时间复杂度O(n*n!)，其中n为数组长度，n!为叶子节点个数。
"""


class Solution:
    def permutation(self, s: str):
        mark = [0] * len(s)
        res, temp = set(), []

        def dfs(u):
            if u == len(s):
                res.add(''.join(temp))
                return
            for i in range(len(s)):
                if not mark[i]:
                    temp.append(s[i])
                    mark[i] = 1
                    dfs(u + 1)
                    temp.pop()
                    mark[i] = 0

        dfs(0)
        return list(res)


solution = Solution()
s = "aab"
print(solution.permutation(s))
