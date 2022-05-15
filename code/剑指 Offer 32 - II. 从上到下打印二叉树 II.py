"""
剑指 Offer 32 - II. 从上到下打印二叉树 II
从上到下按层打印二叉树，同一层的节点按从左到右的顺序打印，每一层打印到一行。
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
  [9,20],
  [15,7]
]
"""
""" 题解
BFS。初始化队列 while len(q): t=q.popleft() 扩展t，注意当前队列大小即为当前层的全部元素长度。
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
            res.append(temp)
        return res
