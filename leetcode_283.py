"""
LeetCode 283：移动零
难度：Easy

题目：将数组中的所有零移动到末尾，保持非零元素的相对顺序。
必须原地修改数组，不复制数组；方法无需返回结果。

算法思路：同向双指针
1. read 指针遍历数组，write 指针记录下一个非零元素的写入位置。
2. 遇到非零元素时，将其写入 nums[write]，然后移动 write。
3. 遍历结束后，将 write 到数组末尾的位置全部补零。

时间复杂度：O(n)
额外空间复杂度：O(1)（不计测试用例占用的空间）
"""


class Solution:
    def moveZeroes(self, nums):
        read = 0
        write = 0

        while read < len(nums):
            if nums[read] != 0:
                nums[write] = nums[read]
                write += 1
            read += 1

        for i in range(write, len(nums)):
            nums[i] = 0


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        ([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]),
        ([0], [0]),
        ([1], [1]),
        ([0, 0, 0], [0, 0, 0]),
        ([1, 2, 3], [1, 2, 3]),
        ([0, 0, 1, 2], [1, 2, 0, 0]),
        ([1, 2, 0, 0], [1, 2, 0, 0]),
        ([0, -1, 0, -1, 2, 0], [-1, -1, 2, 0, 0, 0]),
    ]

    for nums, expected in test_cases:
        original = nums.copy()
        original_reference = nums
        result = solution.moveZeroes(nums)
        print(f"{original} -> {nums}，预期：{expected}")
        assert nums == expected, f"原地修改结果不符合预期：{nums}"
        assert nums is original_reference, "必须保留原列表对象"
        assert result is None, "方法无需返回结果"

    print(f"全部 {len(test_cases)} 个测试通过。")
