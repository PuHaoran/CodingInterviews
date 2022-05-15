"""
剑指 Offer 29. 顺时针打印矩阵
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。



示例 1：

输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,2,3,6,9,8,7,4,5]
示例 2：

输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
输出：[1,2,3,4,8,12,11,10,9,5,6,7]
"""
""" 题解
按照右、下、左、上的顺序遍历数组，其中起始位置位于(0,-1)，走下一步之前先进行正确性的判断。
"""


class Solution:
    def spiralOrder(self, matrix):
        m = len(matrix)
        if m == 0:
            return []
        n = len(matrix[0])
        mark = [[0]*n for _ in range(m)]
        i, j, t = 0, -1, 0
        res = []
        while t < m * n:
            while j+1<n and not mark[i][j+1]:
                j += 1
                t += 1
                mark[i][j] = 1
                res.append(matrix[i][j])
            while i+1<m and not mark[i+1][j]:
                i += 1
                t += 1
                mark[i][j] = 1
                res.append(matrix[i][j])
            while j-1>=0 and not mark[i][j-1]:
                j -= 1
                t += 1
                mark[i][j] = 1
                res.append(matrix[i][j])
            while i-1>=0 and not mark[i-1][j]:
                i -= 1
                t += 1
                mark[i][j] = 1
                res.append(matrix[i][j])
        return res


matrix = []
solution = Solution()
print(solution.spiralOrder(matrix))
