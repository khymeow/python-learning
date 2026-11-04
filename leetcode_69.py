"""
LeetCode 69：x 的平方根
英文名称：Sqrt(x)
难度：Easy
题目地址：https://leetcode.cn/problems/sqrtx/
学习日期：2026 年 11 月 4 日
核心知识点：二分查找、闭区间、候选答案、向下取整、边界更新。

题目：给定非负整数 x，返回平方根向下取整后的整数，不使用内置平方根函数
或浮点幂运算直接求解。例如 x=8 返回 2，x=0 返回 0。

整理来源：本地未发现用户保存的第 69 题最终代码，因此按用户授权采用本简化版本。
此版本包含 AI 辅助讲解，用户已理解，不声称完全由用户独立编写。
用户提到已在线提交过本题，但本次没有可靠的 Accepted 结果佐证，不确认在线通过。

解题思路：在整数闭区间 [0, x] 内寻找满足 mid * mid <= x 的最大整数。
1. left=0、right=x、answer=0，使用 while left <= right 检查所有候选位置。
2. mid * mid <= x 时，mid 是合法候选，保存 answer=mid，并向右寻找更大的合法值。
3. mid * mid > x 时，只令 right=mid-1，不将过大的值记录为答案。
4. 区间为空后，返回最后保存的合法答案。
时间复杂度：O(log x)，通常按 x >= 2 分析；x 为 0 或 1 时只需常数次操作。
额外空间复杂度：O(1)，仅保存固定数量的整数变量。

真实学习过程与修正：
1. 第一次尝试使用 left、right、mid，但曾用 while left < right，结束后返回 mid // 1。
   这可能漏掉最后一个候选；最后一次 mid 不一定正确，x=0 时还可能未初始化 mid。
2. 曾用普通除法计算 mid，得到浮点数；误以为对 mid 向下取整即可得到平方根。
   后来理解应维护整数搜索范围，不能仅依赖最后一次 mid。
3. 用户曾独立写出通过检查 mid ** 2、(mid+1) ** 2、(mid-1) ** 2 判断答案的版本。
   这版逻辑正确，但判断分支较多；不能将这一阶段描述为完全不会做。
4. 简化时曾将 mid ** 2 < x 和 mid ** 2 > x 分别放入两个 while。
   二分过程中大小关系可能交替变化，两个独立循环无法正确处理这种变化。
   例如 x=8 时，该错误版本可能返回 4，正确结果应为 2；这是学习复盘中的示例。
5. 经 AI 辅助讲解，理解本题只记录平方不超过 x 的合法候选，并继续向右寻找最大值。
   用户总结：“只要小的，不要大的，因为最后答案是向下取整。”
   准确含义是本题只在 mid * mid <= x 时更新 answer，包含相等情况；
   这不是所有二分查找都只能记录较小值的通用规则。仍需巩固边界与独立实现。
"""


class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        answer = 0

        while left <= right:
            mid = (left + right) // 2

            if mid * mid <= x:
                answer = mid
                left = mid + 1
            else:
                right = mid - 1

        return answer


if __name__ == "__main__":
    solution = Solution()

    tests = [
        (0, 0),
        (1, 1),
        (2, 1),
        (3, 1),
        (4, 2),
        (8, 2),
        (9, 3),
        (15, 3),
        (16, 4),
        (24, 4),
        (27, 5),
        (100, 10),
        (101, 10),
        (2147395599, 46339),
        (2147483647, 46340),
    ]

    for index, (x, expected) in enumerate(tests, start=1):
        result = solution.mySqrt(x)
        print(f"测试 {index}：x={x}，结果={result}，预期={expected}")
        assert result == expected, f"测试 {index} 失败：{result} != {expected}"

    print(f"全部 {len(tests)} 组测试通过！")
