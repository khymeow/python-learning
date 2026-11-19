"""
LeetCode 112：路径总和
英文名称：Path Sum
难度：Easy
题目地址：https://leetcode.cn/problems/path-sum/

判断是否存在从根节点到叶子节点的路径，其节点值之和等于 targetSum。
DFS 每层减去当前节点值，将剩余目标传给子节点。到达叶子且余量为 0 时返回 True。
用 or 连接左右递归调用，左侧找到合法路径时跳过右侧。
最坏时间复杂度 O(n)，额外空间复杂度 O(h)，其中 n 为节点数，h 为树高。

学习复盘：首版独立完成，短路求值优化在讲解后自行实现。
题目允许负数节点，因此保留对剩余目标值为零或负数时的搜索。
"""


def hasPathSum(root, targetSum):
    if not root:
        return False

    num = targetSum - root.val

    if not root.left and not root.right and num == 0:
        return True

    re = (
        hasPathSum(root.left, targetSum - root.val)
        or hasPathSum(root.right, targetSum - root.val)
    )
    return re


class Solution:
    def hasPathSum(self, root, targetSum):
        return hasPathSum(root, targetSum)
