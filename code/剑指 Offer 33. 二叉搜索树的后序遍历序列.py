"""
剑指 Offer 33. 二叉搜索树的后序遍历序列
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。如果是则返回 true，否则返回 false。假设输入的数组的任意两个数字都互不相同。



参考以下这颗二叉搜索树：

     5
    / \
   2   6
  / \
 1   3
示例 1：

输入: [1,6,3,2,5]
输出: false
示例 2：

输入: [1,3,2,6,5]
输出: true
"""
""" 题解
根节点位于最右边，找到第一个大于根节点的索引，其到根节点之间的所有节点为右子树，其之前的所有节点为左子树；
若只有一个节点或右子树比根节点小则递归终止，否则继续递归dfs(左子树)&&dfs(右子树)。
"""


class Solution:
    def verifyPostorder(self, postorder):
        def dfs(postorder, l, r):
            if l >= r:
                return True
            x = postorder[r]
            for i in range(l, r+1):
                if postorder[i] > x:
                    break
            for j in range(i, r):
                if postorder[j] <= x:
                    return False
            return dfs(postorder, l, i-1) and dfs(postorder,i, r-1)
        return dfs(postorder, 0, len(postorder)-1)


postorder = [1,3,2,6,5]
solution = Solution()
print(solution.verifyPostorder(postorder))
