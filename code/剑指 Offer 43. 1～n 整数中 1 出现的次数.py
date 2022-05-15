"""
剑指 Offer 43. 1～n 整数中 1 出现的次数
输入一个整数 n ，求1～n这n个整数的十进制表示中1出现的次数。

例如，输入12，1～12这些整数中包含1 的数字有1、10、11和12，1一共出现了5次。



示例 1：

输入：n = 12
输出：5
示例 2：

输入：n = 13
输出：6
"""
"""
abcdefg
   0    abc*1000 ?
   1    abc*1000 + efg+1
   >1   (abc+1)*1000
"""


class Solution:
    def countDigitOne(self, n: int) -> int:
        arr = []
        while n:
            arr.append(n%10)
            n //= 10
        arr = arr[::-1]
        print(arr)
        res = 0
        for i in range(len(arr)):
            l, r, p = 0, 0, 1
            for j in range(i):
                l = l * 10 + arr[j]
            for j in range(i+1, len(arr)):
                r = r * 10 + arr[j]
                p *= 10
            if arr[i] == 0:
                res += l * p
            elif arr[i] == 1:
                res += l * p + r + 1
            else:
                res += (l+1) * p
        return res
