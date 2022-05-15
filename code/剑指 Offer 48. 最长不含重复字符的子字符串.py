"""
剑指 Offer 48. 最长不含重复字符的子字符串
请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度。



示例 1:

输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
"""
""" 题解
遍历数组，设置一个双向队列存储无重复子串，当前元素不在队列中则直接加入队列，当前元素若已在队列中则从左边弹出元素直至队列中不再存在当前元素。
"""
import collections


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        q = collections.deque()
        s = list(s)
        res = 0
        for i in range(len(s)):
            if s[i] in q:
                while 1:
                    t = q.popleft()
                    if t == s[i]:
                        break
            q.append(s[i])
            res = max(res, len(q))
        return res
