"""
LeetCode 101：对称二叉树
英文名称：Symmetric Tree
难度：Easy
题目地址：https://leetcode.cn/problems/symmetric-tree/

给定二叉树的根节点，判断整棵树的结构和节点值是否关于根节点镜像对称。
从根节点与自身开始做双节点递归。两个节点都为空时返回 True，恰好一个为空时返回 False。
两个节点都存在时先比较节点值，再分别比较左子树与对侧右子树、右子树与对侧左子树，
最后用 and 汇总结果。

最坏时间复杂度 O(n)，额外空间复杂度 O(h)，来自递归调用栈。
n 为节点数，h 为树高。

学习复盘：最初没有想到如何从第 100 题迁移到镜像比较。经提示理解左右交叉对应后，
在填空练习中自行补出 right 和 left，并理解镜像位置需要同时检查结构和节点值。
随后独立写出完整递归，从 is_mirror(root, root) 开始比较。
"""


def is_symmetric(root):
    def is_mirror(p, q):
        if (p is None and q is not None) or (q is None and p is not None):
            return False
        elif p is not None and q is not None:
            if p.val != q.val:
                return False
            else:
                left_same = is_mirror(p.left, q.right)
                right_same = is_mirror(p.right, q.left)
                return left_same and right_same
        else:
            return True

    return is_mirror(root, root)


class Solution:
    def isSymmetric(self, root):
        return is_symmetric(root)
