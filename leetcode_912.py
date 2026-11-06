"""
LeetCode 912：排序数组
英文名称：Sort an Array
难度：Medium
题目地址：https://leetcode.cn/problems/sort-an-array/
学习记录日期：2026 年 11 月 6 日
核心知识点：随机基准、三路划分、递归边界、递归返回值、列表拼接。

题目：给定整数数组 nums，按非递减顺序排序并返回，不使用内置排序函数。
题目要求 O(n log n) 时间复杂度，并尽量降低额外空间开销。

保留用户最终完成的随机基准三路快速排序，不替换算法或改为原地实现。
解题思路：
1. 空列表或单元素列表直接返回，作为递归边界。
2. random.choice(nums) 随机选择基准值。
3. 将元素分入小于、等于、大于基准值的 left、equal、right 三个列表。
4. 只递归排序 left 和 right，equal 中的重复元素不再参与递归。
5. 接收两侧的递归返回值，依次 extend(equal)、extend(right)，返回 left。
Solution.sortArray 仅调用原 quick_sort，提供题目对应的方法入口。

平均时间复杂度：O(n log n)；最坏时间复杂度：O(n²)。
随机基准降低持续出现极端不平衡划分的概率，但不能保证最坏 O(n log n)。
全部元素相等时，一轮划分即可处理所有元素，时间为 O(n)。
最坏额外空间复杂度：O(n²)。不是原地排序；极端不平衡时，多层递归
同时保留长度约为 n、n-1、n-2 等的新列表。递归栈最坏深度为 O(n)，
还可能受到 Python 递归深度限制。测试辅助数据不计入解法空间复杂度。

学习复盘：
1. 普通两路划分若未有效排除重复元素，可能在大量重复值下严重失衡；
   三路划分把等于基准值的元素集中保存，避免它们继续参与递归。
2. 基准值随机化改善平均表现，但不能消除最坏情况。
3. left = quick_sort(left)、right = quick_sort(right) 必须接收递归结果。
4. extend() 修改原列表并返回 None，不能将其返回值作为排序结果；
   这是需要理解的语义，不额外认定用户曾写出对应错误。
当前已完成此代码练习，递归、分治、复杂度分析和独立复现仍需巩固。
"""

import random


def quick_sort(nums: list[int]) -> list[int]:
    if len(nums) <= 1:
        return nums

    x = random.choice(nums)
    left = []
    equal = []
    right = []

    for i in nums:
        if i == x:
            equal.append(i)
        elif i < x:
            left.append(i)
        else:
            right.append(i)

    left = quick_sort(left)
    right = quick_sort(right)

    left.extend(equal)
    left.extend(right)

    return left


class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        return quick_sort(nums)


if __name__ == "__main__":
    random.seed(912)
    tests = [
        ([], []),
        ([42], [42]),
        ([5, 2, 3, 1], [1, 2, 3, 5]),
        ([5, 1, 1, 2, 0, 0], [0, 0, 1, 1, 2, 5]),
        ([-2, -5, 0, 3, -2], [-5, -2, -2, 0, 3]),
        (list(range(50)), list(range(50))),
        (list(range(49, -1, -1)), list(range(50))),
        ([2] * 50000, [2] * 50000),
        ([-50000, 50000, 0], [-50000, 0, 50000]),
    ]

    for index, (nums, expected) in enumerate(tests, start=1):
        for name, method in [
            ("quick_sort", quick_sort),
            ("Solution.sortArray", Solution().sortArray),
        ]:
            original = nums[:]
            result = method(nums)
            assert result == expected, f"测试 {index}（{name}）排序结果错误"
            assert nums == original, f"测试 {index}（{name}）修改了输入列表"
        print(f"测试 {index}：PASS（两个入口，元素数量 {len(nums)}）")

    print(f"全部 {len(tests)} 组测试通过，两个入口共验证 {len(tests) * 2} 次！")
