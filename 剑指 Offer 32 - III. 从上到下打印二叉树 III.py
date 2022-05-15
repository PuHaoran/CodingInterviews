"""
剑指 Offer 32 - III. 从上到下打印二叉树 III
请实现一个函数按照之字形顺序打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右到左的顺序打印，第三行再按照从左到右的顺序打印，其他行以此类推。



例如:
给定二叉树: [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：

[
  [3],
  [20,9],
  [15,7]
]
"""
""" 题解
BFS实现层次遍历，输出时根据奇偶打印。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode):
        if not root:
            return []
        res = []
        from collections import deque
        q = deque()
        q.append(root)
        i = 1
        while len(q):
            cnt = len(q)
            temp = []
            for _ in range(cnt):
                t = q.popleft()
                temp.append(t.val)
                if t.left:
                    q.append(t.left)
                if t.right:
                    q.append(t.right)
            if i % 2:
                res.append(temp)
            else:
                res.append(temp[::-1])
            i += 1
        return res
