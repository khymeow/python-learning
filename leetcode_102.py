"""
LeetCode 102：二叉树的层序遍历
英文名称：Binary Tree Level Order Traversal
难度：Medium
题目地址：https://leetcode.cn/problems/binary-tree-level-order-traversal/

给定二叉树的根节点，按从上到下、从左到右的顺序访问节点，逐层返回节点值。
使用 deque 实现 BFS。每轮开始时用 level_size 记下当前层的节点数，
内层循环只处理这些节点。新入队的子节点留到下一轮，当前层结束后将 level 加入 result。

时间复杂度 O(n)。额外空间复杂度 O(n)，不计返回结果，队列最多保存 O(n) 个节点。
n 为二叉树的节点数。

学习复盘：在独立完成一维 BFS 后，自行搭建二维 BFS 的双层循环，并按提示修正两处问题。
1. queue.popleft 缺少括号，得到方法对象，访问 num.val 时会报属性错误。
2. 漏写 result.append(level)，修正后在内层 for 结束时保存当前层。
另一次接口报错源于缺少 Solution 类。归档时将独立函数 level_order(root) 的逻辑放入
Solution.levelOrder(self, root)，保留原有 BFS 实现。
"""

from collections import deque


class Solution:
    def levelOrder(self, root):
        if root is None:
            return []

        queue = deque([root])
        result = []

        while queue:
            level_size = len(queue)
            level = []

            for i in range(level_size):
                num = queue.popleft()
                level.append(num.val)

                if num.left is not None:
                    queue.append(num.left)

                if num.right is not None:
                    queue.append(num.right)

            result.append(level)

        return result
