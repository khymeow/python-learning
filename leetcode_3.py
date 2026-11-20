"""
LeetCode 3：无重复字符的最长子串
英文名称：Longest Substring Without Repeating Characters
难度：Medium
题目地址：https://leetcode.cn/problems/longest-substring-without-repeating-characters/

给定字符串 s，求没有重复字符的最长连续子串的长度。
核心知识点：可变长度滑动窗口、用 set 维护成员状态、待加入字符和窗口边界。

每次检查 s[right] 前，seen 保存半开区间 [left, right) 内的字符。如果
s[right] 尚未出现，就加入它并更新 maxlen，再继续扩张。若已出现，就逐个
移除左侧字符并右移 left，直到当前右侧字符能够加入。每个字符最多进出集合
各一次，按集合操作平均 O(1) 计，时间 O(n)，额外空间 O(min(n, 字符集大小))。

学习复盘：初版用 set(s[left:right+1]) 等写法反复构建集合，可以得到正确
结果，但重复处理窗口数据，按窗口最长可达 n 的一般情况分析，时间上界 O(n²)。
优化时曾把左指针移错方向，窗口无法正确收缩，可能陷入死循环。修正后每次
移除左端字符就执行 left += 1。也曾在右指针已到末尾后继续访问 s[right]，
改为最后一个字符成功入窗并更新最长长度后直接返回。将 seen = set() 移到
循环外，才能保留上一轮的窗口状态。

曾担心从集合删除左侧字符后，集合和窗口不同步。检查重复时，右端待加入的
字符还在窗口外，当前窗口内部的字符互不重复。删除左端字符并推进左指针后，
集合仍对应收缩后的窗口，待加入的字符留到下一轮检查。
完成方式：自行编写初版，经多轮针对性指导和自行修改完成优化。
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        maxlen=0
        left=0
        right=0
        seen=set()
        while left<=right:
            if s[right] not in seen:
                seen.add(s[right])
                maxlen=max(maxlen,right-left+1)
                if right==len(s)-1:
                    return maxlen
                else:
                    right+=1
            else:
                seen.remove(s[left])
                left+=1
        return maxlen
