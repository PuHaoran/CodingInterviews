"""
剑指 Offer 26. 树的子结构
输入两棵二叉树A和B，判断B是不是A的子结构。(约定空树不是任意一个树的子结构)

B是A的子结构， 即 A中有出现和B相同的结构和节点值。

例如:
给定的树 A:

     3
    / \
   4   5
  / \
 1   2
给定的树 B：

   4
  /
 1
返回 true，因为 B 与 A 的一个子树拥有相同的结构和节点值。

示例 1：

输入：A = [1,2,3], B = [3,1]
输出：false
示例 2：

输入：A = [3,4,5,1,2], B = [4,1]
输出：true
"""
""" 题解
递归。判断B是否是A的子树需要从A的各个节点进行判断，故我们需要二个递归，一个用来比较从根节点开始是否相等，一个用来遍历A的所有节点。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        if not A or not B:
            return False

        def dfs(A, B):
            if not B:
                return True
            if not A:
                return False
            if A.val != B.val:
                return False
            return dfs(A.left, B.left) and dfs(A.right, B.right)
        res = dfs(A, B)
        return res or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B)
