"""
LeetCode 206：反转链表
英文名称：Reverse Linked List
难度：Easy
题目地址：https://leetcode.cn/problems/reverse-linked-list/
学习日期：2026 年 11 月 2 日

题目：反转单链表的 next 引用，返回反转后的新头节点；空链表返回 None。
例如 1 -> 2 -> 3 -> None 变为 3 -> 2 -> 1 -> None，不是只交换节点数值。

解题思路：三个引用变量的迭代反转
prev 指向已经反转部分的头节点，current 指向当前待处理节点，
next_node 保存原本的后继。每轮严格按以下四步操作：
1. next_node = current.next：先保存后继，避免断开后无法访问剩余链表。
2. current.next = prev：反转当前节点的引用，第一轮也会将原头节点指向 None。
3. prev = current：更新已反转部分的头节点。
4. current = next_node：继续处理尚未反转的部分。
循环条件使用 current is not None，全部节点处理完后返回 prev。

复杂度分析：设节点数为 n。
时间复杂度：O(n)，每个节点处理一次。
额外空间复杂度：O(1)，只使用固定数量的引用变量，反转过程不新建节点。
下面的链表构造、转换和节点身份检查仅用于本地测试，其空间不计入解法。

真实学习过程与错误复盘（均已修正）：
1. 开始时已练习 ListNode、next 连接、current = current.next 遍历、
   中间插入删除、删除头尾节点和部分 None 边界，但还不知道如何反转整条链表。
   最初想移动到尾节点再让其指向 head，分析后发现这只会成环，不会完成反转。
2. 从 a -> b -> None 理解局部反转：b.next = a，再令 a.next = None。
   后面还有节点时，必须先保存后继，才能安全修改 next。
3. 初版使用 current、cnext、ccnext，循环条件叠加 current.next.next.next。
   因此前已改变 next，条件访问到 None.next，触发 AttributeError。
   后来改用职责清楚的 prev、current、next_node，避免沿已修改的引用寻找后继。
4. 某版 while next_node is not None 漏处理最后一个节点，需循环后补反转。
   逐步追踪后理解：while 每轮开始前判断条件，不会每执行一行就重新判断。
5. 改为 while current is not None 后，曾在循环末尾有条件地更新 next_node，
   导致尾节点处引用未更新、重复处理，可能成环；最终每轮开头无条件保存后继。
6. 另一版仍在循环前写 next_node = current.next，空链表时触发
   AttributeError: 'NoneType' object has no attribute 'next'。
   删除该初始化，仅在循环内保存后继，空链表与单节点即可统一处理。
7. 最终版本在多次独立尝试和针对性讲解后完成，已理解变量移动与终止条件，
   仍需间隔复现检验熟练程度，不能描述为第一次就完全独立写对。
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head

        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        return prev


def build_linked_list(values):
    """本地测试辅助：将普通列表转换为链表。"""
    head = None
    tail = None
    for value in values:
        node = ListNode(value)
        if head is None:
            head = node
        else:
            tail.next = node
        tail = node
    return head


def has_cycle(head):
    """本地测试辅助：使用快慢引用检查结果是否成环。"""
    slow = fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False


def linked_list_to_list(head):
    """本地测试辅助：转换为普通列表；若成环则报错，避免无限遍历。"""
    if has_cycle(head):
        raise ValueError("链表存在环，无法转换为普通列表")
    values = []
    current = head
    while current is not None:
        values.append(current.val)
        current = current.next
    return values


if __name__ == "__main__":
    tests = [
        ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
        ([1, 2], [2, 1]),
        ([1], [1]),
        ([], []),
        ([1, 2, 3], [3, 2, 1]),
        ([10, 20, 30, 40], [40, 30, 20, 10]),
        ([1, 1, 2, 2], [2, 2, 1, 1]),
    ]

    for index, (values, expected) in enumerate(tests, start=1):
        head = build_linked_list(values)
        original_nodes = []
        current = head
        while current is not None:
            original_nodes.append(current)
            current = current.next

        result = Solution().reverseList(head)
        assert not has_cycle(result), f"测试 {index}：反转后出现环"
        actual = linked_list_to_list(result)
        assert actual == expected, f"测试 {index}：实际 {actual}，预期 {expected}"

        # 逐个比较对象身份，确保节点本身按逆序连接，而非复制节点或交换 val。
        current = result
        for node in reversed(original_nodes):
            assert current is node, f"测试 {index}：未按逆序使用原有节点"
            current = current.next
        assert current is None, f"测试 {index}：结果含有额外节点"
        assert [node.val for node in original_nodes] == values, (
            f"测试 {index}：原有节点数值被改变"
        )
        if not values:
            assert result is None, "空链表应返回 None"

        print(f"测试 {index}: PASS（输入：{values}，结果：{actual}）")

    print("全部 7 组测试通过，原有节点身份与数值保持一致，结果无环。")
