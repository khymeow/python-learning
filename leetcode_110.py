"""
LeetCode 110：平衡二叉树
英文名称：Balanced Binary Tree
难度：Easy
题目地址：https://leetcode.cn/problems/balanced-binary-tree/

给定二叉树的根节点，判断树中每个节点的左右子树高度差是否都不超过 1。

最终实现使用后序 DFS。空子树高度为 0，平衡的子树返回实际高度，不平衡的子树返回 -1。
先求左子树高度，再求右子树高度，收到 -1 就立即向上传递。
两侧都平衡时，根据当前节点的高度差返回 -1 或 max(lh, rh) + 1。
最坏时间复杂度 O(n)，额外空间复杂度 O(h)，来自递归调用栈。

早期实现对左右子树分别做 BFS 计算高度，再对两侧递归判断平衡。不同递归层会重复计算
子树高度，时间复杂度上界为 O(n²)。额外空间复杂度 O(w + h)，来自队列和递归调用栈。
n 为节点数，h 为树高，w 为树的最大层宽。

学习复盘：先自行尝试 BFS + DFS，经纠错完成。层序求高时修正了队列初始化、循环条件、
子节点入队、当前层长度的读取时机和高度初值。后来理解空树判平衡返回 True、求高度返回 0，
并补上对整棵树各个节点的平衡检查。O(n) 版本先经 AI 完整讲解，再通过强化训练掌握
高度返回和 -1 的传播过程，最后根据步骤提示独立重写完整实现。
"""

from collections import deque


def is_balanced(root):
    def check_height(node):
        if not node:
            return 0

        lh = check_height(node.left)

        if lh == -1:
            return -1

        rh = check_height(node.right)

        if rh == -1:
            return -1

        if abs(lh - rh) > 1:
            return -1

        return max(lh, rh) + 1

    return check_height(root) != -1


class Solution:
    def isBalanced(self, root):
        return is_balanced(root)


def is_balanced_bfs(root):
    """早期练习版本：BFS 求子树高度，DFS 判断整棵树是否平衡。"""
    if not root:
        return True

    def tree_height(root):
        if not root:
            return 0

        queue = deque([root])
        height = 0

        while queue:
            level_size = len(queue)

            for _ in range(level_size):
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            height += 1

        return height

    lh = tree_height(root.left)
    rh = tree_height(root.right)

    if abs(lh - rh) > 1:
        return False
    else:
        left_balanced = is_balanced_bfs(root.left)
        right_balanced = is_balanced_bfs(root.right)
        return left_balanced and right_balanced
