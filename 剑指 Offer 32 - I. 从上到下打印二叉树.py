"""
剑指 Offer 32 - I. 从上到下打印二叉树
从上到下打印出二叉树的每个节点，同一层的节点按照从左到右的顺序打印。



例如:
给定二叉树: [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回：

[3,9,20,15,7]
"""
""" 题解
BFS，初始化队列 while queue.qsize: t=q.put() 扩展t，注意当前队列大小即为当前层的全部元素长度。
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
            t = q.popleft()
            res.append(t.val)
            if t.left:
                q.append(t.left)
            if t.right:
                q.append(t.right)
        return res
