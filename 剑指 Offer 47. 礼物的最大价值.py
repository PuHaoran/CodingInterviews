"""
剑指 Offer 47. 礼物的最大价值
在一个 m*n 的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值（价值大于 0）。你可以从棋盘的左上角开始拿格子里的礼物，并每次向右或者向下移动一格、直到到达棋盘的右下角。给定一个棋盘及其上面的礼物的价值，请计算你最多能拿到多少价值的礼物？
示例 1:
输入:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 12
解释: 路径 1→3→5→2→1 可以拿到最多价值的礼物
"""
""" 动态规划解法
①动态表达 f(i, j)，第i,j步能拿到的最大价值。
②动态转移 f(i,j)=max(f(i-1,j), f(i,j-1))+arr[i][j]。
"""


class Solution:
    def maxValue(self, grid) -> int:
        n, m = len(grid), len(grid[0])
        f = [[0]*(m+1) for _ in range(n+1)]
        for i in range(1, n+1):
            for j in range(1, m+1):
                f[i][j] = max(f[i-1][j], f[i][j-1]) + grid[i-1][j-1]
        return f[n][m]


grid = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
solution = Solution()
print(solution.maxValue(grid))

""" DFS解法
深搜，找到所有路径，记录最大值并返回。（会超时）
"""


class Solution:
    def maxValue(self, grid):
        global res
        m, n = len(grid), len(grid[0])
        mark = [[0]*n for _ in range(m)]
        res = 0
        dx, dy = [1, 0], [0, 1]

        def dfs(i, j, t):
            global res
            t += grid[i][j]
            if i == m-1 and j == n-1:
                res = max(res, t)
                return
            for k in range(2):
                x, y = i + dx[k], j + dy[k]
                if x >= 0 and x < m and y >= 0 and y < n and not mark[x][y]:
                    mark[x][y] = 1
                    dfs(x, y, t)
                    mark[x][y] = 0
        dfs(0, 0, 0)
        return res
