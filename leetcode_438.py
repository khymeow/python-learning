"""
LeetCode 438：找到字符串中所有字母异位词
英文名称：Find All Anagrams in a String
难度：Medium
题目地址：https://leetcode.cn/problems/find-all-anagrams-in-a-string/

返回字符串 s 中所有由 p 的字符重新排列得到的子串的起始下标。字母异位词
的每种字符及其出现次数都相同，排列顺序可以不同。
核心知识点：固定长度滑动窗口、字典频次、字典相等比较、删除计数为零的键。

用 dic() 统计 p 和首个窗口的频次，随后比较 dic1 和 dic2。若相等就记录
left。移动窗口时减少离开字符的计数，归零时删除其键，再增加进入字符的计数。
右指针到达字符串末尾后停止添加字符。

复杂度以 n = len(s)、m = len(p) 计。扫描阶段每次只更新两个字符，
小写英文字母的频次字典最多 26 个键，因此每次比较和更新为 O(1)，
扫描总时间 O(n)，两个频次字典额外空间 O(1)。计入初始化后的总时间
O(n + m)，当 m <= n 时为 O(n)。除输出外，原实现的首窗切片会占用
最多 O(min(n, m)) 的临时空间。

学习复盘：独立写出的第一版使用内部函数 dic() 为每个窗口重新统计频次，
结果正确。随后主动改用动态字典，只更新进出窗口的字符。学习了
del dic[key] 会删除键值对，而值为 0 的键仍会参与字典相等性比较，
因此窗口内没有某字符时要移除其键。曾遇到
TypeError: string indices must be integers, not 'str'，由此区分
字符串用整数取字符和频次字典用字符作键。动态字典初版在最后一个窗口
比较后仍右移并读取 s[right]，导致越界。自行加入 if right<len(s)-1，
把右移和加入字符放到该判断下。
完成方式：第一版独立完成，动态字典优化版经边界纠错后自行完成。
"""


class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        left=0
        right=len(p)-1
        result=[]
        def dic(a):
            dic={}
            for i in a:
                if i in dic:
                    dic[i]+=1
                else:
                    dic[i]=1
            return dic
        dic1=dic(p)
        dic2=dic(s[left:right+1])
        for _ in range(len(s)-len(p)+1):
            if dic1 == dic2:
                result.append(left)
            if dic2[s[left]] == 1:
                del dic2[s[left]]
            else:
                dic2[s[left]]-=1
            left+=1
            if right<len(s)-1:
                right+=1
                if s[right] in dic2:
                    dic2[s[right]]+=1
                else:
                    dic2[s[right]]=1
                
        return result
