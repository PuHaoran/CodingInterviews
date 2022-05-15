"""
剑指 Offer 07. 重建二叉树
输入某二叉树的前序遍历和中序遍历的结果，请构建该二叉树并返回其根节点。

假设输入的前序遍历和中序遍历的结果中都不含重复的数字。

示例 1:


Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
示例 2:

Input: preorder = [-1], inorder = [-1]
Output: [-1]
"""
""" 题解
根据前序数组的首元素可确定根节点，根据中序数组可确定该根节点对应的左右子树。
然后，根据确定的左/右子树的前序数组和中序数组继续递归。
伪代码：root.left = dfs(左子树前序数组，左子树中序数组)；root.right = dfs(右子树前序数组，右子树中序数组)。

 3 9 20 15 7
 pl        pr
 9 3 15 20 7
 il        ir
  idx

# 左子树前序、中序
#pl+1  pl+idx-il        il idx-1
# 右子树前序、中序
#pr-(ir-idx-1)  pr            idx+1 ir

Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
示例 2:

Input: preorder = [-1], inorder = [-1]
Output: [-1]
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder, inorder):
        def dfs(preorder, pre_l, pre_r, inorder, in_l, in_r):
            if pre_r < pre_l:
                return None
            idx = inorder.index(preorder[pre_l])
            root = TreeNode(preorder[pre_l])
            root.left = dfs(preorder, pre_l + 1, pre_l + idx - in_l, inorder, in_l, idx - 1)
            root.right = dfs(preorder, pre_l + idx - in_l + 1, pre_r, inorder, idx + 1, in_r)
            return root

        pre_l, pre_r, in_l, in_r = 0, len(preorder) - 1, 0, len(inorder) - 1
        root = dfs(preorder, pre_l, pre_r, inorder, in_l, in_r)
        return root
