"""
LeetCode 111：二叉树的最小深度
英文名称：Minimum Depth of Binary Tree
难度：Easy
题目地址：https://leetcode.cn/problems/minimum-depth-of-binary-tree/

返回从根节点到最近叶子节点的路径包含的节点数。空树深度为 0。
递归求左右子树的深度。只有一侧子树时，取该子树的深度加 1；
两侧都存在时取较小深度加 1，叶子节点则由两侧深度 0 得到 1。
时间复杂度 O(n)，额外空间复杂度 O(h)，其中 n 为节点数，h 为树高。

学习复盘：独立写出第一版并主动发现单侧子树的边界问题。
理解空子树无法构成根到叶子的路径后，根据提示自行修正各层的递归逻辑。
"""


def minDepth(root):
    if not root:
        return 0

    leftn = minDepth(root.left)
    rightn = minDepth(root.right)

    if root.left and not root.right:
        return leftn + 1

    if root.right and not root.left:
        return rightn + 1
    else:
        return min(leftn, rightn) + 1


class Solution:
    def minDepth(self, root):
        return minDepth(root)
