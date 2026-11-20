"""
LeetCode 209：长度最小的子数组
英文名称：Minimum Size Subarray Sum
难度：Medium
题目地址：https://leetcode.cn/problems/minimum-size-subarray-sum/

给定非空正整数数组 nums 和正整数 target，求和至少为 target 的最短连续
子数组长度。没有符合条件的子数组时返回 0。
核心知识点：可变长度滑动窗口、窗口和、扩张与收缩、最短长度的更新时机。

用 sums 保存闭区间 [left, right] 的和。如果 sum(nums) < target，由于元素均为
正数，任何子数组的和都达不到目标。窗口和不足时向右扩张，右端已到末尾时
结束。窗口和达到目标时，先用 right-left+1 更新 minlen，再移除左端元素，
尝试更短的窗口。求总和与双指针扫描合计时间 O(n)，额外空间 O(1)。

学习复盘：从固定窗口过渡到可变窗口时，自行设计了扩张、收缩和总和预判。
讨论 while left <= right 时，AI 曾质疑退出条件。用户指出，在此实现中，
只有先记录一个合法的单元素窗口再移除其左端元素，left 才会超过 right。
此时最短长度已为 1，退出条件成立。由此厘清了窗口状态、更新最短长度的
时机以及指针交错的含义。
完成方式：自行设计实现，经过讨论和纠错完成，并主动纠正了 AI 对循环条件的判断。
"""


class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left=0
        right=0
        minlen=len(nums)
        sums=nums[0]
        if sum(nums)<target:
            return 0
        while left<=right:
            if sums<target:
                if right==len(nums)-1:
                    break
                else:
                    right+=1
                    sums+=nums[right]
            else:
                minlen=min(minlen,right-left+1)
                sums-=nums[left]
                left+=1
        return minlen
