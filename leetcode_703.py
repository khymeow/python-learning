"""
LeetCode 703：数据流中的第 K 大元素
英文名称：Kth Largest Element in a Stream
难度：Easy
题目地址：https://leetcode.cn/problems/kth-largest-element-in-a-stream/

用整数 k 和初始数组 nums 创建 KthLargest。每次调用 add(val) 将 val
加入数据流，并返回所有已加入的数字（包括初始数组）中第 k 大的值。
重复数字分别计入排名。
核心知识点：对象属性、原地建最小堆、跨调用维护堆状态、Top K。

构造方法保存 self.k，并用 heapify 原地将 self.nums 建成最小堆。
每次 add 先压入新元素，堆长超过 k 时反复弹出最小值。这样保留最大的
k 个值，其中最小的一个位于堆顶，即第 k 大。初始数组的超量元素在
首次 add 中删除，构造方法只建堆。

设初始长度为 n。构造时间 O(n)，首次 add 删除 max(0, n + 1 - k) 个
元素，按堆操作计，时间上界为 O((1 + max(0, n + 1 - k)) log(n + 2))。
裁剪后，每次 add 的摊还时间为 O(log(k + 1))。堆复用并原地修改调用者
传入的列表，未复制初始数据。列表从初始 n 个元素变为每次 add 后至多
k 个，维护阶段的堆状态占 O(k)，堆操作本身只需 O(1) 辅助空间。

学习复盘：先复习 __init__ 在创建对象时自动调用、self.k 在多次调用间
保留，而普通局部变量只属于当前调用。早期曾把 minh = [] 写在 add 内，
导致每次重新建列表。改用 self.minh 后，一度仍在每次 add 中重加部分
初始数据，造成重复。最终用 self.nums 保存同一个堆并持续更新。

一开始误以为 heapify 会排序，试图从堆尾截取最大的 k 个元素。最小堆
只保证父节点不大于子节点，只有堆顶保证最小。self.nums[-1:-self.k-1]
的起点在终点右侧，默认正步长下得到空列表。还复习了 append 将整个
列表追加为一个元素、extend 将列表元素逐个追加的区别。

曾在插入后无条件弹出堆顶，理解保留候选数后改为只在堆长大于 k 时弹出。
曾在每次 add 中重新 heapify，结果正确但重复建堆。经讲解，主动把建堆
移到 __init__，之后由 heappush 和 heappop 保持堆性质。
完成方式：经多轮提示与纠错后自行完成最终代码。
"""


import heapq


class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.k=k
        self.nums=nums
        heapq.heapify(self.nums)

    def add(self, val: int) -> int:
        heapq.heappush(self.nums,val)
        while len(self.nums)>self.k:
            heapq.heappop(self.nums)
        return self.nums[0]
