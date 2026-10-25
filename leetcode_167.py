"""
LeetCode 167：两数之和 II — 输入有序数组
难度：Medium

题目：给定按非递减顺序排列的数组 numbers 和目标值 target，
找到和为 target 的两个数，返回从 1 开始的下标，且不能重复使用同一元素。
题目保证恰好存在一个解。

算法思路：双指针
1. left 和 right 分别从数组两端开始。
2. 两数之和大于目标值时，左移 right；小于目标值时，右移 left。
3. 两数之和等于目标值时，返回两个指针位置加 1。

时间复杂度：O(n)
额外空间复杂度：O(1)
"""


class Solution:
    def twoSum(self, numbers, target):
        left = 0
        right = len(numbers) - 1

        while left < right:
            if numbers[left] + numbers[right] > target:
                right -= 1
            elif numbers[left] + numbers[right] < target:
                left += 1
            else:
                return [left + 1, right + 1]


def two_sum_sorted(numbers, target):
    """提供函数入口，方便独立运行测试；算法保留在 Solution.twoSum 中。"""
    return Solution().twoSum(numbers, target)


if __name__ == "__main__":
    print(two_sum_sorted([2, 7, 11, 15], 9))      # [1, 2]
    print(two_sum_sorted([2, 3, 4], 6))           # [1, 3]
    print(two_sum_sorted([-1, 0], -1))           # [1, 2]
    print(two_sum_sorted([1, 1, 2, 3], 2))        # [1, 2]
    print(two_sum_sorted([1, 2, 3, 4, 4, 9], 8))  # [4, 5]
