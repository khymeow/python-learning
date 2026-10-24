
"""
LeetCode 1207：独一无二的出现次数
难度：Easy

题目：
给定一个整数数组 arr，如果每个数字的出现次数都是
独一无二的，返回 True，否则返回 False。

解题思路：
1. 使用字典统计每个数字出现的次数。
2. 将所有出现次数保存到列表。
3. 使用 set() 对出现次数去重。
4. 如果去重前后长度相等，说明出现次数没有重复。

时间复杂度：O(n)
空间复杂度：O(n)
"""


def count_numbers(nums):
    num_dict = {}
    for num in nums:
        if num not in num_dict:
            num_dict[num] = 1
        else:
            num_dict[num] += 1

    return num_dict


def unique_occurrences(arr):
    nums = []
    for value in count_numbers(arr).values():
        nums.append(value)

    return len(set(nums)) == len(nums)


if __name__ == "__main__":
    print(unique_occurrences([1, 2, 2, 1, 1, 3]))
    # True

    print(unique_occurrences([1, 2]))
    # False

    print(unique_occurrences([-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]))
    # True
