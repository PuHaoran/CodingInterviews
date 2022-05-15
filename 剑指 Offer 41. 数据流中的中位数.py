"""
剑指 Offer 41. 数据流中的中位数
如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。

例如，

[2,3,4] 的中位数是 3

[2,3] 的中位数是 (2 + 3) / 2 = 2.5

设计一个支持以下两种操作的数据结构：

void addNum(int num) - 从数据流中添加一个整数到数据结构中。
double findMedian() - 返回目前所有元素的中位数。
示例 1：

输入：
["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"]
[[],[1],[2],[],[3],[]]
输出：[null,null,null,1.50000,null,2.00000]
示例 2：

输入：
["MedianFinder","addNum","findMedian","addNum","findMedian"]
[[],[2],[],[3],[]]
输出：[null,null,2.00000,null,2.50000]
"""
""" 题解
|_____|___|
   A    B
大/小顶堆。维护A、B两个堆，A保存较小元素，B保存较大元素；A使用大顶堆存储，B使用小顶堆存储。
findMedian: A == B，AB各弹出一个求平均；否则，B弹出一个。
addNum: A == B，将元素入B，然后弹出一个最小值入A；否则，将元素入A，然后弹出一个最大值入B。
"""
from heapq import *
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.a = []
        self.b = []

    def addNum(self, num: int) -> None:
        if len(self.a) == len(self.b):
            heappush(self.b, num)
            heappush(self.a, -heappop(self.b))
        else:
            heappush(self.a, -num)
            heappush(self.b, -heappop(self.a))

    def findMedian(self) -> float:
        return (-self.a[0] + self.b[0]) / 2.0 if len(self.a) == len(self.b) else -self.a[0]
