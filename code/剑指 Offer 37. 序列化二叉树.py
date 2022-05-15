"""
剑指 Offer 37. 序列化二叉树
请实现两个函数，分别用来序列化和反序列化二叉树。

你需要设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列 / 反序列化算法执行逻辑，你只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串反序列化为原始的树结构。

提示：输入输出格式与 LeetCode 目前使用的方式一致，详情请参阅LeetCode 序列化二叉树的格式。你并非必须采取这种方式，你也可以采用其他的方法解决这个问题。

示例：
输入：root = [1,2,3,null,null,4,5]
输出：[1,2,3,null,null,4,5]
"""
""" 题解
通过两次层序遍历进行序列化和反序列化；其中反序列化过程可通过一个指针指向当前节点所对应的孩子节点。
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''
        from collections import deque
        q = deque()
        res = []
        q.append(root)
        while len(q):
            t = q.popleft()
            if t:
                res.append(str(t.val))
                q.append(t.left)
                q.append(t.right)
            else:
                res.append('None')
        return ','.join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not len(data):
            return
        from collections import deque
        q = deque()
        s = data.split(',')
        root = TreeNode(int(s[0]))
        q.append(root)
        i = 1
        while len(q):
            t = q.popleft()
            if s[i] == 'None':
                t.left = None
            else:
                node = TreeNode(int(s[i]))
                t.left = node
                q.append(node)
            i += 1
            if s[i] == 'None':
                t.right = None
            else:
                node = TreeNode(int(s[i]))
                t.right = node
                q.append(node)
            i += 1
        return root
