"""
LeetCode 876：链表的中间结点
英文名称：Middle of the Linked List
难度：Easy
题目地址：https://leetcode.cn/problems/middle-of-the-linked-list/
学习日期：2026 年 11 月 3 日
核心知识点：链表遍历、长度统计、快慢指针、短路求值。

题目：给定非空单链表，返回中间节点；偶数长度时返回第二个中间节点。
[1, 2, 3, 4, 5] 返回节点 3；[1, 2, 3, 4, 5, 6] 返回节点 4。

正式思路：slow 每轮走一步，fast 每轮走两步。
当 fast 到达末尾时，slow 位于中间；从相同起点移动，偶数长度会停在第二个中间。
时间复杂度：O(n)，遍历链表的长度数量级。
额外空间复杂度：O(1)，仅使用两个移动引用。

真实学习过程：
1. 最初独立提出两次遍历：先统计长度 num，再移动到中间。
   奇数的 (num - 1) / 2 与偶数的 num / 2，后来统一为整数步数 num // 2，
   用 for i in range(num // 2) 固定移动次数。独立写出的第一版忘记 return head，
   补上后逻辑正确，下方保留为 middle_node_two_pass，依赖题目保证的非空输入。
2. 随后学习快慢指针，最终独立写出并验证了正式版本。
   最初认为只需 while fast.next is not None，但偶数长度可能使 fast 先变为 None。
   应使用 fast is not None and fast.next is not None，利用 and 从左到右短路，
   确认对象非空后才访问 next。
3. 两次遍历与快慢指针均为 O(n) 时间、O(1) 额外空间，前者是正确的学习版本。
测试构造与结果转换的空间不计入上述解法复杂度。
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        return slow


def middle_node_two_pass(head):
    """用户独立完成的两次遍历参考法，仅用于题目保证的非空链表。"""
    num = 1
    current = head

    while current.next is not None:
        num += 1
        current = current.next

    for i in range(num // 2):
        head = head.next

    return head


def build_linked_list(values):
    """测试辅助：创建链表与用于身份检查的原节点列表。"""
    nodes = [ListNode(value) for value in values]
    for left, right in zip(nodes, nodes[1:]):
        left.next = right
    return (nodes[0] if nodes else None), nodes


def linked_list_to_list(head):
    """测试辅助：转换整段后缀，若出现环则报错而非无限遍历。"""
    values = []
    seen = set()
    while head is not None:
        assert id(head) not in seen, "FAIL：返回链表出现环"
        seen.add(id(head))
        values.append(head.val)
        head = head.next
    return values


if __name__ == "__main__":
    tests = [
        ([1], [1]),
        ([1, 2], [2]),
        ([1, 2, 3], [2, 3]),
        ([1, 2, 3, 4], [3, 4]),
        ([1, 2, 3, 4, 5], [3, 4, 5]),
        ([1, 2, 3, 4, 5, 6], [4, 5, 6]),
    ]

    for index, (values, expected) in enumerate(tests, 1):
        for name, method in [
            ("快慢指针", Solution().middleNode),
            ("两次遍历", middle_node_two_pass),
        ]:
            head, nodes = build_linked_list(values)
            original_next = [node.next for node in nodes]
            result = method(head)
            actual = linked_list_to_list(result)
            assert actual == expected, f"FAIL {index} {name}：实际 {actual}，预期 {expected}"
            assert result is nodes[len(nodes) // 2], f"FAIL {index} {name}：中间节点身份错误"
            assert all(node.next is nxt for node, nxt in zip(nodes, original_next)), (
                f"FAIL {index} {name}：原链表连接被改变"
            )
            print(f"测试 {index}（{name}）: PASS（后缀：{actual}）")

    print("全部 6 组测试通过，两种方法各验证 6 组！")
