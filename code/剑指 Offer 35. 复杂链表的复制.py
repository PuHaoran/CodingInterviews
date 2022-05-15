"""
剑指 Offer 35. 复杂链表的复制
请实现 copyRandomList 函数，复制一个复杂链表。在复杂链表中，每个节点除了有一个 next 指针指向下一个节点，还有一个 random 指针指向链表中的任意节点或者 null。

示例 1：
输入：head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
输出：[[7,null],[13,0],[11,4],[10,2],[1,0]]
示例 2：

输入：head = [[1,1],[2,1]]
输出：[[1,1],[2,1]]
"""
""" 题解
复制链表各节点在原链表节点后，然后遍历链表根据原链表random节点的下一个节点即为新链表对应的random节点，得到复制链表。
"""


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        p = head
        while p:
            p_next = p.next
            q = Node(p.val)
            p.next = q
            q.next = p_next
            p = p_next
        new_head = Node(-1)
        h = new_head
        p = head
        while p:
            q = p.next
            p_random = p.random
            if not p_random:
                q_random = None
            else:
                q_random = p_random.next
            q.random = q_random
            h.next = q
            h = h.next
            p = q.next
        return new_head.next
