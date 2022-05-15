"""
剑指 Offer 40. 最小的k个数
输入整数数组 arr ，找出其中最小的 k 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。



示例 1：

输入：arr = [3,2,1], k = 2
输出：[1,2] 或者 [2,1]
示例 2：

输入：arr = [0,1,2,1], k = 1
输出：[0]
"""
""" 题解
堆排序，构建1-n的数组，然后从倒数第一个非叶子节点从后向前遍历，down(i)以递归方式进行节点位置的调整，判断当前节点与孩子节点大小并交换(若交换则按交换的孩子位置继续down)。
"""


class Solution:
    def getLeastNumbers(self, arr, k: int):
        global n
        n = len(arr)
        arr = [0] + arr

        def down(i):
            t = i
            if 2*i<=n and arr[2*i] < arr[t]:
                t = 2*i
            if 2*i+1<=n and arr[2*i+1] < arr[t]:
                t = 2*i+1
            if i != t:
                arr[i], arr[t] = arr[t], arr[i]
                down(t)
        for i in range(n//2, 0, -1):
            down(i)
        res = []
        for _ in range(k):
            res.append(arr[1])
            arr[1], arr[n] = arr[n], arr[1]
            n -= 1
            down(1)
        return res


arr = [1, 3, 2, 4, 5]
k = 3
solution = Solution()
print(solution.getLeastNumbers(arr, k))


""" 题解
利用快排模版解题。[_A_][__B__]，若k的个数<=A长度则只递归A（最小的k个值在A区间里），否则只递归B并更新k-=A区间长度（A区间的值都满足最小的k个值，同时有一部分k-A长度个值在B区间里）。
"""


class Solution:
    def getLeastNumbers(self, arr, k: int):
        def quick_sort(arr, l, r, k):
            if l >= r:
                return
            x = arr[l]
            i, j = l - 1, r + 1
            while i < j:
                while 1:
                    i += 1
                    if arr[i] >= x:
                        break
                while 1:
                    j -= 1
                    if arr[j] <= x:
                        break
                if i < j:
                    arr[i], arr[j] = arr[j], arr[i]
            if k <= j-l+1:
                quick_sort(arr, l, j, k)
            else:
                quick_sort(arr, j+1, r, k-(j-l+1))
        quick_sort(arr, 0, len(arr)-1, k)
        return arr[:k]


arr = [0,1,2,1]
k = 1
solution = Solution()
print(solution.getLeastNumbers(arr, k))
