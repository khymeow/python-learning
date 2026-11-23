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

在完成 sum_tree() 求和练习后独立写出首版，学习时反馈本地测试通过。
首版先计算左右递归结果再用 or 合并，此时两次调用均已执行。理解短路后，
自行把两次递归调用直接放在 or 两侧。曾讨论复用 num，最终仍按
targetSum - root.val 传参。

还主动讨论了全正数树的剪枝：先处理当前叶子是否恰好命中，再判断能否继续
向下。后续节点值均严格为正时，剩余目标值小于等于 0 即可停止向下搜索；
本题允许负数，最终代码未采用这一剪枝。
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
