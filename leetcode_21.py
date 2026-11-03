"""
LeetCode 21：合并两个有序链表
英文名称：Merge Two Sorted Lists
难度：Easy
题目地址：https://leetcode.cn/problems/merge-two-sorted-lists/
学习日期：2026 年 11 月 3 日
核心知识点：链表归并、节点连接、双指针、边界判断。

题目：将两个非递减单链表合并为一个有序链表，返回合并后的头节点。
例如 [1, 2, 4] 与 [1, 3, 4] 合并为 [1, 1, 2, 3, 4, 4]。

自己的迭代思路（不使用虚拟头节点）：
1. 用 a、b 遍历两个链表；其中一个为空时，直接返回另一个。
2. 从两个首节点中选较小者作为 head 与 tail，并移动被选链表的引用。
3. 两者都未耗尽时，每次将较小节点接到 tail.next，再移动 tail 和被选引用。
4. 其中一条耗尽后，直接连接另一条已经有序的剩余部分，返回固定的 head。
tail.next = a 修改节点连接；tail = a 只是移动变量引用。

复杂度：设两条链表长度为 m、n。
时间复杂度：O(m + n)，每个节点最多参与一次归并处理。
额外空间复杂度：O(1)，只移动固定数量的引用，复用原有节点。
下方构造链表及身份检查仅用于测试，不计入解法的空间。

真实错误复盘（均已修正）：
1. 最初比较方向写成 >=，会优先选择较大值；初始化与循环统一修正为 <=。
2. 曾使用 while a.next is not None and b.next is not None：
   a 或 b 为 None 时访问 next 会报错；尾节点的 next 为空但节点本身仍需处理。
   改为检查 a、b 本身，使循环执行到其中一条真正耗尽。
3. 剩余部分曾通过 a.next、b.next 是否为空判断，同样混淆了尾节点与耗尽。
   a is None 时连接剩余 b，b is None 时连接剩余 a。
4. head 保留起点，tail 保留结果尾部；每次只移动被选中的输入引用。
学习中曾对“循环内最后一次连接”与“循环外剩余连接”的提问含义产生混淆，
当时实际连接代码正确，不将该讨论记成程序错误。
代码由用户自己写出，经上述错误修正后通过测试，正式方案保留迭代结构。
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self,
        list1: Optional[ListNode],
        list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        a = list1
        b = list2

        if a is None:
            return b
        if b is None:
            return a

        if a.val <= b.val:
            tail = a
            a = a.next
        else:
            tail = b
            b = b.next

        head = tail

        while a is not None and b is not None:
            if a.val <= b.val:
                tail.next = a
                tail = a
                a = a.next
            else:
                tail.next = b
                tail = b
                b = b.next

        if a is None:
            tail.next = b
        elif b is None:
            tail.next = a

        return head


def build_linked_list(values):
    """测试辅助：创建链表，同时保留有限的原节点列表用于身份验证。"""
    nodes = [ListNode(value) for value in values]
    for left, right in zip(nodes, nodes[1:]):
        left.next = right
    return (nodes[0] if nodes else None), nodes


def collect_nodes(head):
    """测试辅助：收集节点，遇到重复对象立即报错，避免有环时无限遍历。"""
    nodes = []
    seen = set()
    while head is not None:
        assert id(head) not in seen, "FAIL：合并结果出现环"
        seen.add(id(head))
        nodes.append(head)
        head = head.next
    return nodes


if __name__ == "__main__":
    tests = [
        ([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4]),
        ([], [], []),
        ([], [0], [0]),
        ([1], [], [1]),
        ([1, 3, 5], [2, 4, 6], [1, 2, 3, 4, 5, 6]),
        ([1, 2], [3, 4], [1, 2, 3, 4]),
        ([1, 1, 2], [1, 2, 2], [1, 1, 1, 2, 2, 2]),
        ([-5, -1, 3], [-3, 0, 7, 9], [-5, -3, -1, 0, 3, 7, 9]),
    ]

    for index, (values1, values2, expected) in enumerate(tests, 1):
        head1, nodes1 = build_linked_list(values1)
        head2, nodes2 = build_linked_list(values2)
        originals = nodes1 + nodes2
        original_values = [node.val for node in originals]
        result = Solution().mergeTwoLists(head1, head2)
        result_nodes = collect_nodes(result)
        actual = [node.val for node in result_nodes]
        assert actual == expected, f"FAIL {index}：实际 {actual}，预期 {expected}"
        assert {id(node) for node in result_nodes} == {id(node) for node in originals}, (
            f"FAIL {index}：结果未完整复用输入节点"
        )
        assert [node.val for node in originals] == original_values, (
            f"FAIL {index}：输入节点数值被改变"
        )
        print(f"测试 {index}: PASS（结果：{actual}，原节点复用且无环）")

    print("全部 8 组测试通过！")
