"""
LeetCode 347：前 K 个高频元素
英文名称：Top K Frequent Elements
难度：Medium
题目地址：https://leetcode.cn/problems/top-k-frequent-elements/

给定整数数组 nums 和整数 k，返回出现频率最高的 k 个不同整数。
结果顺序任意，题目保证这组元素唯一。
核心知识点：字典计数、items() 和键值拆包、按元组优先级建堆。

用 dic 统计次数，从 dic.items() 取得 num、times，再把 (-times,num)
放进 list1。Python 按顺序比较元组元素，先比较负频次，相等时再比较
数字。对 list1 建最小堆后弹出 k 次，每次把元组第二项加入 list2。

设 n 为输入长度，m 为不同数字的个数。计数平均 O(n)，构建元组列表
和建堆各为 O(m)，弹出阶段上界 O(k log(m + 1))。总时间上界为
O(n + m + k log(m + 1))。频次字典与堆占 O(m) 额外空间，返回列表
占 O(k)。此写法对全部 m 个不同数字建堆，k 与 m 都接近 n 时，
时间上界可达 O(n log n)，因此无法保证满足题目的进阶复杂度要求。

学习复盘：曾询问 TypeError: unhashable type: 'list'。讨论了列表
不可哈希，无法作为字典键或集合元素，整数、字符串及元素都可哈希的
元组可以作为键。堆本身可以存放可比较的列表。还问过
TypeError: 'builtin_function_or_method' object is not iterable，
由此复习 dic.items 是方法对象，调用 dic.items() 才得到可迭代的
键值对视图，也复习了 keys()、values() 和循环中的键值拆包。
这两次问答均未提供完整触发代码，复盘只记录报错及讨论过的原因。

用户自行将频次取负并与原数字组成元组，用堆按频率取出结果。
完成方式：核心算法独立完成，期间主动询问 Python 类型与字典方法报错。
"""


import heapq


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        dic = {}
        list1=[]
        for num in nums:
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1
        for num, times in dic.items():
            list1.append((-times,num))
        heapq.heapify(list1)
        list2=[]
        for _ in range (k):
            a,b=heapq.heappop(list1)
            list2.append(b)
        return list2
