"""
剑指 Offer 46. 把数字翻译成字符串
给定一个数字，我们按照如下规则把它翻译为字符串：0 翻译成 “a” ，1 翻译成 “b”，……，11 翻译成 “l”，……，25 翻译成 “z”。一个数字可能有多个翻译。请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。



示例 1:

输入: 12258
输出: 5
解释: 12258有5种不同的翻译，分别是"bccfi", "bwfi", "bczi", "mcfi"和"mzi"
"""
""" 题解 
①动态表达 f(i) i个字符前有多少种不同的翻译。
②动态转换 f(i) = f(i-1)+f(i-2)或f(i-1) （PS:新增的字符不满足成双的情况对增加翻译数量无益）
"""


class Solution:
    def translateNum(self, num: int) -> int:
        num = '0'+str(num)
        f = [0] * len(num)
        f[0] = 1
        f[1] = 1
        for i in range(2, len(num)):
            if num[i-1:i+1] >= '10' and num[i-1:i+1] <= '25':
                f[i] = f[i-1] + f[i-2]
            else:
                f[i] = f[i-1]
        return f[len(num)-1]


num = 506
solution = Solution()
print(solution.translateNum(num))
