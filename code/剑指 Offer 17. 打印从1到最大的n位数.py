"""
剑指 Offer 17. 打印从1到最大的n位数
输入数字 n，按顺序打印出从 1 到最大的 n 位十进制数。比如输入 3，则打印出 1、2、3 一直到最大的 3 位数 999。

示例 1:

输入: n = 1
输出: [1,2,3,4,5,6,7,8,9]
"""
"""
利用DFS对数字进行全排列，dfs输入u步数作为递归终止条件，mark数组标记走过的路径，path存储路径。
"""


class Solution:
    def printNumbers(self, n: int):
        def dfs(u):
            if u == n:
                res.append(''.join(path))
                return
            for i in range(10):
                path.append(str(i))
                dfs(u+1)
                path.pop()

        res = []
        path = []
        dfs(0)
        return [int(i) for i in res[1:]]
