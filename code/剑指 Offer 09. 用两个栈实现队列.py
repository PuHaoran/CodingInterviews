"""
剑指 Offer 09. 用两个栈实现队列
用两个栈实现一个队列。队列的声明如下，请实现它的两个函数 appendTail 和 deleteHead ，分别完成在队列尾部插入整数和在队列头部删除整数的功能。(若队列中没有元素，deleteHead 操作返回 -1 )

示例 1：
输入：
["CQueue","appendTail","deleteHead","deleteHead"]
[[],[3],[],[]]
输出：[null,null,3,-1]
示例 2：

输入：
["CQueue","deleteHead","appendTail","appendTail","deleteHead","deleteHead"]
[[],[],[5],[2],[],[]]
输出：[null,-1,null,null,5,2]
"""
""" 题解
使用A和B两个栈模拟队列的插入和删除操作。进队列直接看做进入A栈，出队列操作需要把A栈数据全部倒入B栈，然后弹出栈顶元素。
注意B栈为空时才能将A栈数据全部倒入，否则直接弹出B栈现存的栈顶元素即可。

eg: 进a b c，然后出a，进d，出b，进e
c
b
a
----------------
   b
   c
----------------
   b
d  c
----------------
d  c
----------------
e
d c
"""


class CQueue:

    def __init__(self):
        self.top1, self.top2 = -1, -1
        self.s1, self.s2 = [0]*1010, [0]*1010

    def appendTail(self, value: int) -> None:
        self.top1 += 1
        self.s1[self.top1] = value

    def deleteHead(self) -> int:
        if self.top1 == -1 and self.top2 == -1:
            return -1
        if self.top2 == -1:
            while self.top1 != -1:
                t = self.s1[self.top1]
                self.top1 -= 1
                self.top2 += 1
                self.s2[self.top2] = t
        t = self.s2[self.top2]
        self.top2 -= 1
        return t
