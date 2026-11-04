"""
自定义二分查找巩固练习：寻找最后一个小于或等于 target 的元素位置
学习日期：2026 年 11 月 4 日
核心知识点：非递减数组、闭区间二分查找、合法候选下标、边界初始化。
本题不是 LeetCode 官方题目，不计入 LeetCode 题解数量。

题目：给定允许重复元素的非递减整数数组 nums，返回最后一个满足 nums[i] <= target
的下标；不存在则返回 -1。例如 [1, 2, 2, 4]、target=2，返回 2。

用户最终独立修正的思路：搜索闭区间 [0, len(nums)-1]，answer 初始化为 -1。
当前元素不超过 target 时保存 mid，并继续向右；否则向左缩小范围。
循环结束后返回最后保存的合法下标。空数组的闭区间初始就为空，自动返回 -1。
时间复杂度：O(log n)，n 为数组长度；空数组为 O(1)。
额外空间复杂度：O(1)。

真实学习过程与修正：
1. 最初 right=len(nums)，会把不存在的末尾下标纳入范围，可能越界；应减 1。
2. 最初 answer=0，不能通用地表示不存在合法答案；改用 -1。
3. 曾添加 if left + 1 >= len(nums) - 1: return answer，试图解决越界问题。
   经分析后理解应修正搜索区间，而不是用特殊提前返回条件掩盖越界。
4. 用户最后独立提交本修正版，并准确总结问题主要在 right、answer 的初始化。
   本版本无需为空数组单独增加分支。
"""


class Solution:
    def findLastLE(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        answer = -1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] <= target:
                answer = mid
                left = mid + 1
            else:
                right = mid - 1

        return answer


if __name__ == "__main__":
    solution = Solution()

    tests = [
        ([1, 3, 5, 7], 5, 2),
        ([1, 3, 5, 7], 4, 1),
        ([1, 3, 5, 7], 0, -1),
        ([1, 3, 5, 7], 9, 3),
        ([1, 2, 2, 2, 4], 2, 3),
        ([2, 2, 2], 2, 2),
        ([2, 2, 2], 1, -1),
        ([-5, -3, -3, 0, 2], -3, 2),
        ([-5, -3, -3, 0, 2], -4, 0),
        ([], 1, -1),
        ([5], 5, 0),
        ([5], 4, -1),
        ([5], 6, 0),
    ]

    for index, (nums, target, expected) in enumerate(tests, start=1):
        result = solution.findLastLE(nums, target)
        print(f"测试 {index}：nums={nums}，target={target}，结果={result}，预期={expected}")
        assert result == expected, f"测试 {index} 失败：{result} != {expected}"

    print(f"全部 {len(tests)} 组测试通过！")
