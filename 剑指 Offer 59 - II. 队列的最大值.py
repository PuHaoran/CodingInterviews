"""
剑指 Offer 59 - II. 队列的最大值
请定义一个队列并实现函数 max_value 得到队列里的最大值，要求函数max_value、push_back 和 pop_front 的均摊时间复杂度都是O(1)。

若队列为空，pop_front 和 max_value 需要返回 -1

示例 1：

输入:
["MaxQueue","push_back","push_back","max_value","pop_front","max_value"]
[[],[1],[2],[],[],[]]
输出: [null,null,null,2,1,2]
示例 2：

输入:
["MaxQueue","pop_front","max_value"]
[[],[],[]]
输出: [null,-1,-1]
"""
"""
双端队列。一个队列用于存储原始数据，另外维持一个单调递减的双端队列用于取出最大值。
"""


class MaxQueue:

    def __init__(self):
        from collections import deque
        self.q1 = deque()
        self.q2 = deque()

    def max_value(self) -> int:
        if not len(self.q2):
            return -1
        return self.q2[0]

    def push_back(self, value: int) -> None:
        while len(self.q2) and value > self.q2[-1]:
            self.q2.pop()
        self.q2.append(value)
        self.q1.append(value)

    def pop_front(self) -> int:
        if not len(self.q1):
            return -1
        t = self.q1.popleft()
        if t == self.q2[0]:
            self.q2.popleft()
        return t
