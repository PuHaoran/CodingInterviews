"""
剑指 Offer 55 - II. 平衡二叉树
输入一棵二叉树的根节点，判断该树是不是平衡二叉树。如果某二叉树中任意节点的左右子树的深度相差不超过1，那么它就是一棵平衡二叉树。



示例 1:

给定二叉树 [3,9,20,null,null,15,7]

    3
   / \
  9  20
    /  \
   15   7
返回 true 。

示例 2:

给定二叉树 [1,2,2,3,3,null,null,4,4]

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
返回 false 。
"""
""" 题解
DFS。遍历当前树并返回左右子树深度，若左右子树深度>1，说明不为平衡二叉树。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        global res
        res = True

        def dfs(root):
            global res
            if not root:
                return 0
            l_depth = dfs(root.left)+1
            r_depth = dfs(root.right)+1
            if abs(l_depth - r_depth) > 1:
                res = False
            return max(l_depth, r_depth)
        dfs(root)
        return res
