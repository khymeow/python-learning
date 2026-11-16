"""
LeetCode 226：翻转二叉树
英文名称：Invert Binary Tree
难度：Easy
题目地址：https://leetcode.cn/problems/invert-binary-tree/

给定二叉树根节点，交换每个节点的左右子树，返回翻转后的根节点。
用 DFS 原地修改树结构。遇到空节点就返回 None，其余节点先交换左右子节点引用，
再递归翻转交换后的两棵子树，最后返回当前根节点。

时间复杂度 O(n)，每个节点访问一次。额外空间复杂度 O(h)，来自递归调用栈。
n 为节点数，h 为树高，极端不平衡时递归栈最坏占用 O(n)。

学习复盘：用户先独立写出左右引用的交换语句，拿到函数框架后独立补全两次递归，
并正确处理空树和根节点返回。递归直接修改子树的连接，调用处只需执行递归。
用户反馈本地测试通过。归档时移除了 DFS 中未使用的 deque 导入。
"""


def invert_tree(root):
    if root is None:
        return None

    root.left, root.right = root.right, root.left

    invert_tree(root.left)
    invert_tree(root.right)

    return root


class Solution:
    def invertTree(self, root):
        return invert_tree(root)
