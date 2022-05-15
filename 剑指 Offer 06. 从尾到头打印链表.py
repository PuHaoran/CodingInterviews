"""
剑指 Offer 06. 从尾到头打印链表
输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。

示例 1：
输入：head = [1,3,2]
输出：[2,3,1]
"""
""" 题解
1->3->2
2
3
1
法一：遍历链表的同时，将所有元素入栈，利用栈先进后出特性可以取出所有元素。
法二：递归本质就是一个栈结构，先访问每一个节点，然后将节点添加到结果数组中。
输入：head = [1,3,2]
输出：[2,3,1]
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reversePrint(self, head: ListNode):
        res = []
        def get_reverse(p):
            if p != None:
                get_reverse(p.next)
                res.append(p.val)
        get_reverse(head)
        return res
