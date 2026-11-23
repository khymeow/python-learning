"""
LeetCode 1046：最后一块石头的重量
英文名称：Last Stone Weight
难度：Easy
题目地址：https://leetcode.cn/problems/last-stone-weight/

给定记录石头重量的整数数组 stones。每轮取出最重的两块。重量相同则
两块都消失，重量不同则放回一块重量为两者之差的石头。最后返回剩余的
重量，若全部消失则返回 0。
核心知识点：用负数模拟最大堆、连续弹出堆顶、负数差值。

将重量取负并建最小堆。连续两次 heappop 得到的 a、b 对应最重和次重
的石头，且 a <= b。a < b 时，a-b 恰好是剩余重量的相反数，再将它
压入堆。a == b 时无需压入。原实现也保留了 a > b 的对称分支，
连续出堆时该分支不会触发。结尾将堆顶恢复为正数，空堆返回 0。

设 n 为石头数，建堆 O(n)，每轮出堆两次、最多入堆一次，堆元素至少
减少一个，总时间上界 O(n log n)，存放负重量的堆占 O(n) 额外空间。

学习复盘：独立写出取负和碰撞处理的主体。初版认为 heap[1] 是第二小
元素，先从 heap[0] 和 heap[1] 取值，再做两次出堆。合法最小堆
[-3, -1, -2] 中第二小的是 -2，说明该索引位置无法保证次序。
经提示理解 heappop 会返回当前最小元素并恢复堆性质，随后自行改为
a = heapq.heappop(heap) 和 b = heapq.heappop(heap)，直接使用
出堆的两个值进行差值计算。
完成方式：主体独立写出，堆索引错误经提示后自行修正。
"""


import heapq


class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        heap=[-x for x in stones]
        heapq.heapify(heap)
        while len(heap)>1:
            a=heapq.heappop(heap)
            b=heapq.heappop(heap)
            if a<b:
                heapq.heappush(heap,a-b)
            elif a>b:
                heapq.heappush(heap,b-a)
        if heap:
            return -heap[0]
        else:
            return 0
