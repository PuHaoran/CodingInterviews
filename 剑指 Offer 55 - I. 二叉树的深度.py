"""
剑指 Offer 55 - I. 二叉树的深度
输入一棵二叉树的根节点，求该树的深度。从根节点到叶节点依次经过的节点（含根、叶节点）形成树的一条路径，最长路径的长度为树的深度。

例如：

给定二叉树 [3,9,20,null,null,15,7]，

    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度3 。
"""
""" BFS解法
BFS。记录层次遍历的层数。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        from collections import deque
        q = deque()
        q.append(root)
        res = 0
        while len(q):
            for _ in range(len(q)):
                t = q.popleft()
                if t.left:
                    q.append(t.left)
                if t.right:
                    q.append(t.right)
            res += 1
        return res


""" DFS解法
DFS。当前节点深度等于其max(左孩子深度，右孩子深度)+1。
"""


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        def dfs(root):
            if not root:
                return 0
            return max(dfs(root.left), dfs(root.right))+1
        return dfs(root)
