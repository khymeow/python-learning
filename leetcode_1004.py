"""
LeetCode 1004：最大连续 1 的个数 III
英文名称：Max Consecutive Ones III
难度：Medium
题目地址：https://leetcode.com/problems/max-consecutive-ones-iii/

给定二进制数组 nums，最多可将 k 个 0 翻转为 1，求能得到的最长连续 1
的长度。等价于寻找包含至多 k 个 0 的最长连续子数组。
核心知识点：可变长度滑动窗口、剩余翻转次数、左右指针的更新时机。

用 change 保存剩余翻转次数。右端是 1 时直接将其纳入窗口；右端是 0 且
仍有机会时，消耗一次机会后纳入。每次成功扩张都更新 maxlen。右端是 0
且机会耗尽时，先移动左端，移出 0 就恢复一次机会，再处理当前右端。
当 k 为 0 且空窗口的右端遇到 0 时，左指针先越过该元素，随后的右移将它跳过，
这次计算的长度为 0。
两指针各自只向右移动，时间 O(n)，额外空间 O(1)。

学习复盘：作为滑动窗口基础阶段的综合检验，在未得到算法类型提示和实现
思路的情况下，独立判断题型并完成代码。通过 change 记录进出窗口的 0
如何消耗和归还机会，并用剩余次数决定能否继续扩张。编写时自行调整过
代码，学习记录中仅保留最终实现。
完成方式：独立完成滑动窗口基础阶段的结课综合练习。
"""


class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        left=0
        right=0
        change=k
        maxlen=0
        while right<len(nums):
            if nums[right]==1:
                maxlen=max(maxlen,right-left+1)
                right+=1
            elif change>0:
                change-=1
                maxlen=max(maxlen,right-left+1)
                right+=1
            else:
                if nums[left]==1:
                    left+=1
                else:
                    change+=1
                    left+=1
        return maxlen
