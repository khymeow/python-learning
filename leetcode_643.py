"""
LeetCode 643：子数组最大平均数 I
英文名称：Maximum Average Subarray I
难度：Easy
题目地址：https://leetcode.cn/problems/maximum-average-subarray-i/

给定整数数组 nums 和长度 k，返回所有长度为 k 的连续子数组中的最大平均值。
核心知识点：固定长度滑动窗口、窗口和的增量更新、左右指针的更新顺序。

先将前 k 个元素累加到 add，并用 maxn 保存目前最大的窗口和。每次右移一格，
在旧左指针推进前加上新右端元素、减去旧左端元素，再更新 maxn。每个窗口长度
都为 k，因此只需比较窗口和，最后返回 maxn/k。时间 O(n)，额外空间 O(1)。

学习复盘：初版先移动 left，再减去 nums[left]，减掉的是新窗口的左端元素，
旧左端元素仍留在窗口和里。经针对性纠错，先按
add = add + nums[right] - nums[left] 更新窗口和，再执行 left += 1。
理解一次滑动只需处理新加入和离开的两个元素，窗口和可以直接复用。
完成方式：自行编写，经过针对性纠错完成。
"""


class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        if len(nums)<k:
            return None
        left=0
        right=k-1
        add=0
        for i in range(k):
            add+=nums[i]
        maxn=add
        for _ in range(len(nums)-k):
            right+=1
            add=add+nums[right]-nums[left]
            left+=1
            maxn=max(maxn,add)
        return maxn/k
