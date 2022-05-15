"""
剑指 Offer 68 - II. 二叉树的最近公共祖先
给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

例如，给定如下二叉树:  root = [3,5,1,6,2,0,8,null,null,7,4]

示例 1:

输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
输出: 3
解释: 节点 5 和节点 1 的最近公共祖先是节点 3。
"""
""" 题解
递归终止条件是找到p或q或二者都没找到；
若左右子树都未找到，返回None；若左子树和右子树都可以找到，则该节点是根节点；
若右子树先找到，则左子树先找到的节点为根节点；若左子树先找到，则右子树先找到的节点为根节点。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return None
        if root == p or root == q:
            return root
        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)
        if not l and not r:  # 左右子树都没有p和q
            return None
        if not l:  # 左子树没有，右子树中找到的第一个就是根节点
            return r
        if not r: # 右子树没有，左子树中找到的第一个就是根节点
            return l
        return root # 左右子树都有，当前根就是最近公共节点
