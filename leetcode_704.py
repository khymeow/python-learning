"""
LeetCode 704：二分查找
英文名称：Binary Search
难度：Easy
题目地址：https://leetcode.cn/problems/binary-search/
学习日期：2026 年 11 月 3 日
核心知识点：闭区间二分查找、左右边界、循环条件。

题目：在升序且元素互不重复的整数数组中寻找 target，找到返回下标，否则返回 -1。
例如 nums = [-1, 0, 3, 5, 9, 12]、target = 9，返回 4。

自己的思路：使用闭区间 [left, right] 保存候选范围，每轮比较中间元素。
中间值小于目标时令 left = mid + 1，大于目标时令 right = mid - 1；
相等时返回下标。每轮排除大约一半元素，区间为空时返回 -1。
时间复杂度：O(log n)，每轮将候选范围大致减半。
额外空间复杂度：O(1)，仅保存固定数量的下标。

真实学习过程与修正：
1. 理解有序数组排除一半候选范围后，用户独立写出了二分查找逻辑，已在线提交通过。
2. 最初将 nums[mid] 写成 list[mid]；list 是内置类型，不是传入数组。
   修正为 nums[mid]。这是变量名错误，不是二分查找算法错误。
3. 用户能够独立解释 while left <= right：left == right 时仍有最后一个候选元素。
   例如 [1, 3, 5, 7, 9] 寻找 9，最终 left == right == 4，仍须检查这一轮。
   若本闭区间版本改用 left < right，可能漏掉最后的候选位置。
"""


class Solution:
    def search(self, nums: list[int], target: int) -> int:
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

        return -1


if __name__ == "__main__":
    solution = Solution()

    tests = [
        ([-1, 0, 3, 5, 9, 12], 9, 4),
        ([-1, 0, 3, 5, 9, 12], 2, -1),
        ([5], 5, 0),
        ([5], 3, -1),
        ([1, 3], 3, 1),
        ([], 1, -1),
        ([1, 3, 5, 7, 9], 9, 4),
        ([1, 3, 5, 7, 9], 1, 0),
    ]

    for index, (nums, target, expected) in enumerate(tests, start=1):
        result = solution.search(nums, target)
        print(f"测试 {index}：nums={nums}，target={target}，结果={result}，预期={expected}")
        assert result == expected, f"测试 {index} 失败：{result} != {expected}"

    print(f"全部 {len(tests)} 组测试通过！")
