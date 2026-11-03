"""
LeetCode 141：环形链表
英文名称：Linked List Cycle
难度：Easy
题目地址：https://leetcode.cn/problems/linked-list-cycle/
学习日期：2026 年 11 月 3 日
核心知识点：快慢指针、对象身份判断、环检测。

题目：判断单链表是否有环，存在环返回 True，否则返回 False。
例如 [3, 2, 0, -4] 的尾节点接回第 2 个节点时返回 True；空链表返回 False。

自己的思路：从第 876 题框架改写，slow 每轮一步，fast 每轮两步。
无环时 fast 会到达末尾；有环时两者进入环内，fast 每轮比 slow 多走一步，
相对距离不断变化，最终必然在同一个节点相遇。移动后用 fast is slow 判断。
时间复杂度：O(n)，到达链表末尾或在环内相遇所需步数为节点数量级。
额外空间复杂度：O(1)，只使用两个引用，不依赖集合。

真实学习过程与修正：
1. 用户自己理解并提出了环中快指针会追上慢指针的思路，
   并在第 876 题的快慢指针基础上独立改写。
2. 尝试验证时暂未改 middleNode 名称属于探索阶段，不记作算法认知错误。
3. 最初用 fast.val == slow.val 判断相遇：不同节点可存相同值；
   fast 也可能已变为 None，继续访问 val 会报错。
4. 经讲解改为比较节点引用，使用 fast == slow 后通过 LeetCode。
   当前 ListNode 没有自定义 __eq__，== 按默认对象身份比较；
   为明确表达“引用同一个节点”，按用户要求最终统一为 fast is slow。
5. fast.val == slow.val 比较数值；fast is slow 比较节点对象身份。
测试通过尾节点重新连接已有节点来构造真实环，辅助代码不遍历有环链表。
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if fast is slow:
                return True

        return False


def build_linked_list(values, pos=-1):
    """测试辅助：pos 为尾部连接的零起始下标；-1 表示不连接成环。"""
    nodes = [ListNode(value) for value in values]
    for left, right in zip(nodes, nodes[1:]):
        left.next = right
    if pos != -1:
        if not 0 <= pos < len(nodes):
            raise ValueError("成环位置必须是已有节点的合法下标")
        nodes[-1].next = nodes[pos]
    return (nodes[0] if nodes else None), nodes


if __name__ == "__main__":
    tests = [
        ([3, 2, 0, -4], 1, True),
        ([1, 2], 0, True),
        ([1], 0, True),
        ([1], -1, False),
        ([1, 2, 3], -1, False),
        ([], -1, False),
        ([1, 1, 1], -1, False),
        ([1, 2, 3, 4, 5], 2, True),
    ]

    for index, (values, pos, expected) in enumerate(tests, 1):
        head, nodes = build_linked_list(values, pos)
        original_next = [node.next for node in nodes]
        result = Solution().hasCycle(head)
        assert result is expected, f"FAIL {index}：实际 {result}，预期 {expected}"
        assert all(node.next is nxt for node, nxt in zip(nodes, original_next)), (
            f"FAIL {index}：判环不应修改链表连接"
        )
        print(f"测试 {index}: PASS（节点值：{values}，连接下标：{pos}，有环：{result}）")

    print("全部 8 组测试通过，包含真实环、空链表及同值不同节点！")
