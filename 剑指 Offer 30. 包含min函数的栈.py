"""
剑指 Offer 30. 包含min函数的栈
定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的 min 函数在该栈中，调用 min、push 及 pop 的时间复杂度都是 O(1)。



示例:

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.min();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.min();   --> 返回 -2.
"""
""" 题解
维护两个栈，一个栈保存所有元素，一个栈保存当前<=x的元素。
"""


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.t = -1
        self.min_t = -1
        self.min_stack = [0]*20010
        self.stack = [0]*20010

    def push(self, x: int) -> None:
        self.t += 1
        self.stack[self.t] = x
        if self.min_t == -1 or x <= self.min_stack[self.min_t]:
            self.min_t += 1
            self.min_stack[self.min_t] = x

    def pop(self) -> None:
        if self.stack[self.t] == self.min_stack[self.min_t]:
            self.min_t -= 1
        self.t -= 1

    def top(self) -> int:
        return self.stack[self.t]

    def min(self) -> int:
        return self.min_stack[self.min_t]



# Your MinStack object will be instantiated and called as such:
x = 3
obj = MinStack()
obj.push(x)
obj.pop()
param_3 = obj.top()
param_4 = obj.min()