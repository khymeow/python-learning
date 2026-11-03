"""
LeetCode 35：搜索插入位置
英文名称：Search Insert Position
难度：Easy
题目地址：https://leetcode.cn/problems/search-insert-position/
学习日期：2026 年 11 月 3 日
核心知识点：二分查找、插入位置、return left。

题目：在升序且元素互不重复的数组中寻找 target；存在则返回下标，
不存在则返回按顺序插入的位置。例如 [1, 3, 5, 6] 寻找 2，返回 1。

自己的思路：沿用第 704 题的闭区间二分查找，将未找到时的 return -1 改为 return left。
目标不存在时，下标小于 left 的元素均小于 target，下标大于 right 的元素均大于 target。
循环结束时 left == right + 1，因此 left 为插入位置；right 是最后一个小于目标的
元素下标，可能为 -1。这些结论针对本题的升序、不重复及目标不存在的条件。
时间复杂度：O(log n)，每轮将候选范围大致减半。
额外空间复杂度：O(1)，仅保存固定数量的下标。

真实学习过程与修正：
1. 用户已在线提交通过。本文件根据用户已通过的 704 代码与明确采用的 return left
   变化整理；用户没有在对话中再次粘贴第 35 题完整的实际在线提交代码。
2. 用户最初能判断 [1, 3, 5, 6] 中 2 应插入下标 1，但手动推演曾误判结束边界为
   (left, right) = (1, 1)，随后又尝试 (0, 0)，均遗漏完整的最后一轮。
   正确过程：(0, 3) -> mid=1、值为3、right=0 -> mid=0、值为1、left=1；
   结束时为 (1, 0)。这是手动推演中的误判，不记为实际程序测试失败。
3. 经过推演后，用户自己确认返回 left，并能独立推导 [2, 4, 6, 8, 10, 12]
   寻找 7 时结束边界为 left=3、right=2，进一步理解插入位置的来源。
"""


class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] == target:
                return mid
            else:
                right = mid - 1

        return left


if __name__ == "__main__":
    solution = Solution()

    tests = [
        ([1, 3, 5, 6], 5, 2),
        ([1, 3, 5, 6], 2, 1),
        ([1, 3, 5, 6], 7, 4),
        ([1, 3, 5, 6], 0, 0),
        ([1, 3, 5, 6], 4, 2),
        ([1], 1, 0),
        ([1], 0, 0),
        ([1], 2, 1),
        ([], 1, 0),
        ([2, 4, 6, 8, 10, 12], 7, 3),
    ]

    for index, (nums, target, expected) in enumerate(tests, start=1):
        result = solution.searchInsert(nums, target)
        print(f"测试 {index}：nums={nums}，target={target}，结果={result}，预期={expected}")
        assert result == expected, f"测试 {index} 失败：{result} != {expected}"

    print(f"全部 {len(tests)} 组测试通过！")
