"""
LeetCode 217：存在重复元素
英文名称：Contains Duplicate
难度：Easy
核心知识点：集合 set、成员判断 in、set.add()、循环、条件判断、提前返回。

题目：给定整数数组 nums，如果任意元素出现至少两次，返回 True；
如果所有元素都互不相同，返回 False。

解题思路：集合加提前返回
1. 使用 newnum = set() 创建空集合，记录已经遍历过的数字。
2. 遍历 nums，若 num in newnum，说明发现重复，立即返回 True。
3. 否则执行 newnum.add(num)，记录当前数字，供后续判断使用。
4. 循环结束仍未发现重复元素时，返回 False。

复杂度分析：设数组长度为 n。
时间复杂度：平均 O(n)。每个元素进行一次平均 O(1) 的集合成员判断，
并在必要时执行平均 O(1) 的添加操作。这不是所有情况下的严格最坏时间界。
额外空间复杂度：O(n)，最坏情况下集合需要保存所有不同的元素。

本次学习记录与易错点：
1. 最初考虑过用切片分割数组，后来确认本题不需要分割。
   先判断题目真正需要什么操作，不因记得某种语法而强行使用它。
2. 空集合应使用 set()，而不是 {}，后者创建的是空字典。
   向集合添加元素使用 set.add()；向列表添加使用 list.append()；
   向 deque 队列尾部添加元素则调用队列实例的 append()。
3. 第一版独立完成的写法也是正确解法，先去重，再比较长度：

       newnum = set()
       for num in nums:
           newnum.add(num)
       return len(nums) != len(newnum)

   集合自动去重，原列表与集合的长度不相等，就说明存在重复元素。
   以上仅作为学习记录；正式解法采用下面的提前返回版本。
4. 提前返回版本发现重复时，return True 会立即结束函数，
   不再遍历剩余元素；return False 必须放在循环结束之后。
   两种写法都正确。在集合操作平均 O(1) 的假设下，遍历整个数组时
   两者都属于平均 O(n) 级别；较早发现重复时，提前返回可以减少实际工作量。
"""


class Solution(object):
    def containsDuplicate(self, nums):
        # 使用空集合记录已经出现过的数字
        newnum = set()

        for num in nums:
            # 发现重复元素，立即结束函数
            if num in newnum:
                return True
            newnum.add(num)

        # 所有元素均不同
        return False


if __name__ == "__main__":
    solution = Solution()

    tests = [
        ([1, 2, 3, 1], True),
        ([1, 2, 3, 4], False),
        ([1, 1, 1, 1], True),
        ([5], False),
        ([-1, 0, 1, -1], True),
        ([3, 2, 1, 4, 5, 2], True),
    ]

    for nums, expected in tests:
        result = solution.containsDuplicate(nums)
        print(
            f"输入：{nums}，结果：{result}，预期：{expected}"
        )
        assert result == expected

    print("全部测试通过！")
