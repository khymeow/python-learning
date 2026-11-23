"""
LeetCode 215：数组中的第 K 个最大元素
英文名称：Kth Largest Element in an Array
难度：Medium
题目地址：https://leetcode.cn/problems/kth-largest-element-in-an-array/

给定整数数组 nums 和整数 k（1 <= k <= len(nums)），返回按降序排列
时第 k 个元素的值。重复值分别计入排名。
核心知识点：最小堆、原地建堆、从完整候选集中淘汰最小值、Top K。

先把整个 nums 原地建成最小堆，再弹出 n-k 个最小值。剩下的 k 个值
恰好是原数组最大的 k 个，堆顶是其中最小的一个，即所求。

设 n 为数组长度。heapify 需要 O(n)，弹出阶段上界为 O((n-k) log n)，
总时间 O(n + (n-k) log n)。额外空间 O(1)，复用并修改输入列表。
此写法从整个数组建堆，k 很小时仍需执行接近 n 次出堆。

学习复盘：紧接第 703 题练习。意识到静态数组一次给出，省去了跨调用维护
对象状态的步骤。自行迁移“保留最大的 k 个值，取其中最小值”的思路，
首版正确，期间无需算法提示或纠错。
完成方式：独立一次完成。
"""


import heapq


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        heapq.heapify(nums)
        while len(nums)>k:
            heapq.heappop(nums)
        return nums[0]
