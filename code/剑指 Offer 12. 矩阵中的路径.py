"""
剑指 Offer 12. 矩阵中的路径
给定一个m x n 二维字符网格board 和一个字符串单词word 。如果word 存在于网格中，返回 true ；否则，返回 false 。
单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

示例 1：
输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
输出：true
示例 2：

输入：board = [["a","b"],["c","d"]], word = "abcd"
输出：false
"""
""" 题解
dfs函数传入u作为递归终止条件，数组mark记录走过的路径并回溯，使用剪枝提前终止递归。
当需要判断True/False时，考虑res = dfs() or dfs()。
"""


class Solution:
    def exist(self, board, word: str) -> bool:
        global row, col, n
        row, col, n = len(board), len(board[0]), len(word)
        mark = [[0]*col for _ in range(row)]
        def dfs(u, i, j):
            if u == n:
                return True
            if i < 0 or i >= row or j < 0 or j >= col or mark[i][j] != 0 or word[u] != board[i][j]:
                return False
            dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
            # 等同于flag = dfs(u + 1, i - 1, j) or dfs(u + 1, i + 1, j) or dfs(u + 1, i, j - 1) or dfs(u + 1, i, j + 1)
            flag = 0
            for k in range(4):
                x, y = i + dx[k], j + dy[k]
                mark[i][j] = 1
                flag = flag or dfs(u+1, x, y)
                mark[i][j] = 0
            return flag

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(0, i, j):
                    return True
        return False


board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
solution = Solution()
print(solution.exist(board=board, word=word))
