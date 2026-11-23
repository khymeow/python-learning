"""
LeetCode 104：二叉树的最大深度
英文名称：Maximum Depth of Binary Tree
难度：Easy
题目地址：https://leetcode.cn/problems/maximum-depth-of-binary-tree/

给定二叉树的根节点，返回从根到最远叶子节点的路径上的节点数。空树的深度为 0。
BFS 用 deque 按层遍历，每处理完一层就把深度加 1。时间 O(n)，额外空间最坏 O(n)。
DFS 递归取得左右子树的深度，取较大值再加上当前节点的一层。时间 O(n)，
额外空间 O(h)，其中 n 为节点数，h 为树高，极端不平衡时调用栈最坏占用 O(n)。
Solution.maxDepth 默认调用 DFS，同时保留独立的 BFS 函数。

学习复盘：自行把第 102 题的分层 BFS 改为按层计数。初稿保留了用于收集节点值的 level
列表，核心计数逻辑正确。代码检查后移除列表及追加操作。
学习 DFS 时，起初想把左右深度相加。通过手推单节点和不平衡树，理解最大深度取
max(left_depth, right_depth) + 1，随后独立写出递归核心。节点计数练习进一步巩固了
递归返回值的用法：左右子树的节点数应求和，再加上当前节点。

手推 DFS 时确认空树深度为 0，单节点深度为 1。还推导过一棵不平衡树中
以节点 1、2、4、8 为根的子树深度，依次为 1、2、3、4。
"""

from collections import deque


def max_depth_bfs(root):
    if root is None:
        return 0

    queue = deque([root])
    result = 0

    while queue:
        level_size = len(queue)

        for i in range(level_size):
            num = queue.popleft()

            if num.left is not None:
                queue.append(num.left)

            if num.right is not None:
                queue.append(num.right)

        result += 1

    return result


def max_depth_dfs(root):
    if root is None:
        return 0

    left_depth = max_depth_dfs(root.left)
    right_depth = max_depth_dfs(root.right)

    return max(left_depth, right_depth) + 1


class Solution:
    def maxDepth(self, root):
        return max_depth_dfs(root)
