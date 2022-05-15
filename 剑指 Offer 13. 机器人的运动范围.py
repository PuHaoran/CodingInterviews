"""
剑指 Offer 13. 机器人的运动范围
地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。一个机器人从坐标 [0, 0] 的格子开始移动，它每次可以向左、右、上、下移动一格（不能移动到方格外），也不能进入行坐标和列坐标的数位之和大于k的格子。例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。但它不能进入方格 [35, 38]，因为3+5+3+8=19。请问该机器人能够到达多少个格子？

示例 1：

输入：m = 2, n = 3, k = 1
输出：3
示例 2：

输入：m = 3, n = 1, k = 0
输出：1
提示：

1 <= n,m <= 100
0 <= k <= 20
"""
""" 题解
模版
// 初始化队列
while len(q):
    t = q.pop()
    // 扩展t，入队列
"""


class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        from collections import deque

        def get_digit(i):
            res = 0
            while i:
                res += i % 10
                i = i // 10
            return res

        def check(i, j, k):
            if get_digit(i) + get_digit(j) <= k:
                return True
            return False
        res = 1
        dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
        mark = [[0]*n for _ in range(m)]
        mark[0][0] = 1
        q = deque()
        q.append((0, 0))
        while len(q):
            t = q.pop()
            for i in range(4):
                x, y = t[0] + dx[i], t[1] + dy[i]
                if x >= 0 and x < m and y >= 0 and y < n and not mark[x][y] and check(x, y, k):
                    res += 1
                    mark[x][y] = 1
                    q.append((x, y))
        return res


m, n, k = 1, 2, 0
solution = Solution()
print(solution.movingCount(m, n, k))
