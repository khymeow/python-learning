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

首版直接用 min(leftn, rightn) + 1，单侧为空时会把返回的 0 当成候选。
曾考虑仅在第一层遇到单侧子树时直接返回 1。经讲解明确，单侧情况会出现在
任意一层，而且要统计实际存在的子树深度。自行修正后覆盖了叶子、仅有左
子树、仅有右子树和两侧均有子树四种情况。

之后主动询问能否合并分支，了解了 AI 讲解的简化写法：任一子树深度为 0
时取 max(leftn, rightn) + 1，否则取 min(leftn, rightn) + 1。
正式代码保留自行修正的版本。
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
