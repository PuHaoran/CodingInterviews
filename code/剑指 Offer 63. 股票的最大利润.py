"""
剑指 Offer 63. 股票的最大利润
假设把某股票的价格按照时间先后顺序存储在数组中，请问买卖该股票一次可能获得的最大利润是多少？



示例 1:

输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。
示例 2:

输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
"""
""" 题解
遍历数组，res=max(res, 当前元素-之前元素的最小值)。
"""


class Solution:
    def maxProfit(self, prices):
        if len(prices) <= 1:
            return 0
        res = 0
        t = prices[0]
        for i in range(1, len(prices)):
            res = max(res, prices[i] - t)
            if prices[i] < t:
                t = prices[i]
        return res


prices = [7,1,5,3,6,4]
solution = Solution()
print(solution.maxProfit(prices))
