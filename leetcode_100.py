"""
LeetCode 100：相同的树
英文名称：Same Tree
难度：Easy
题目地址：https://leetcode.cn/problems/same-tree/

给定两棵二叉树的根节点 p 和 q，判断树的结构及对应位置的节点值是否都相同。
用 DFS 比较同一位置上的两个节点。恰好一个为空时返回 False，两个都为空时返回 True。
两个都存在时先比较节点值。值相同才递归比较左右子树，并用 and 合并两个布尔结果。

设两棵树的节点数为 n、m，高度为 hp、hq。最坏时间复杂度 O(min(n, m) + 1)，
每个继续递归的位置都有两个非空节点，其余位置的比较会立即结束。
额外空间复杂度 O(min(hp, hq) + 1)，来自递归调用栈，包含终止调用。

学习复盘：用户独立设计空节点与节点值的判断，主动发现初稿调用子递归后遗漏了返回值，
导致当前层隐式返回 None。经提示，分别用 left_same 和 right_same 接收结果，
再返回 left_same and right_same。原来判断恰好一个节点为空的逻辑正确，体现的是异或 XOR，
归档时用 is None / is not None 规范写法。用户反馈修正后本地测试通过。
"""


def is_same_tree(p, q):
    if (p is None and q is not None) or (q is None and p is not None):
        return False

    elif p is not None and q is not None:
        if p.val != q.val:
            return False
        else:
            left_same = is_same_tree(p.left, q.left)
            right_same = is_same_tree(p.right, q.right)
            return left_same and right_same

    else:
        return True


class Solution:
    def isSameTree(self, p, q):
        return is_same_tree(p, q)
