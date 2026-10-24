"""
LeetCode 1：两数之和
难度：Easy

思路：哈希表
使用字典保存“需要匹配的数字 → 对应索引”。
遍历时先查询，找不到再记录当前数字的补数。

时间复杂度：平均 O(n)
空间复杂度：O(n)
"""


def two_sum(nums, target):
    seen = {}

    for i, num in enumerate(nums):
        if num in seen:
            return [seen[num], i]

        seen[target - num] = i

    return []


if __name__ == "__main__":
    print(two_sum([2, 7, 11, 15], 9))
    print(two_sum([3, 2, 4], 6))
    print(two_sum([3, 3], 6))