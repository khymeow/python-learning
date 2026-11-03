"""
LeetCode 34：在排序数组中查找元素的第一个和最后一个位置
英文名称：Find First and Last Position of Element in Sorted Array
难度：Medium
题目地址：https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/
学习日期：2026 年 11 月 3 日
核心知识点：左右边界二分查找、候选答案、嵌套函数复用。

题目：在非递减数组中返回 target 第一次和最后一次出现的下标；不存在返回 [-1, -1]。
例如 [5, 7, 7, 8, 8, 10] 寻找 8，返回 [3, 4]。

自己的思路：保留嵌套函数 findBoundary(findLeft)，分别执行两次闭区间二分查找。
每次 answer = -1；遇到目标先记录 answer = mid，再朝所需边界继续搜索：
找左边界令 right = mid - 1，找右边界令 left = mid + 1。
若后续未再遇到目标，保留最近一次候选答案；始终未找到则保留 -1。
例如 [1, 2, 5, 5, 5, 5, 7] 寻找 5，最终为 [2, 5]。
时间复杂度：O(log n)，两次 O(log n) 二分查找相加仍为 O(log n)。
额外空间复杂度：O(1)，不计算输入输出占用；函数没有递归调用。

真实学习过程与修正：
1. 用户经过几轮独立尝试和针对性纠错后，最终版本已在线提交通过。
2. 初次使用普通二分找到目标后向两边线性扩展，但未检查 a-1、b+1 的边界。
   a=0 时负索引可能误访问末尾；b 为最后一个下标时 b+1 会触发 IndexError。
   全部元素相同还可能遍历整个数组，退化为 O(n)，因此未采用这一版作为最终解法。
3. 用户自己提出封装二分函数，经讨论形成 findBoundary(findLeft) 分别找左右边界。
   已理解找到相等元素后朝左或朝右缩小范围，找到候选不代表找到最终边界。
4. 曾在更新边界后递归调用 findBoundary(findLeft)，但新调用会重新将左右边界
   初始化为整个数组，可能反复搜索并触发 RecursionError。
   最终删除内部递归调用，只更新边界，让当前 while 自然进入下一轮。
5. 曾使用 answerl=right、answerr=left 初始化，目标不存在时会保留错误下标；
   最终改用 answer=-1，确保未找到目标时返回 -1。
6. 曾用 min(mid, answerl)、max(mid, answerr) 保存结果；边界持续缩小，后续相等
   候选自然更靠所需边界，直接 answer=mid 即可。特别是 min(mid, -1) 总会保留 -1。
"""


class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:

        def findBoundary(findLeft):
            left = 0
            right = len(nums) - 1
            answer = -1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] < target:
                    left = mid + 1

                elif nums[mid] == target:
                    if findLeft:
                        answer = mid
                        right = mid - 1
                    else:
                        answer = mid
                        left = mid + 1

                else:
                    right = mid - 1

            return answer

        a = findBoundary(True)
        b = findBoundary(False)

        return [a, b]


if __name__ == "__main__":
    solution = Solution()

    tests = [
        ([5, 7, 7, 8, 8, 10], 8, [3, 4]),
        ([5, 7, 7, 8, 8, 10], 6, [-1, -1]),
        ([], 0, [-1, -1]),
        ([1], 1, [0, 0]),
        ([1], 2, [-1, -1]),
        ([2, 2, 2, 2, 2], 2, [0, 4]),
        ([1, 1, 2, 3, 4], 1, [0, 1]),
        ([1, 2, 3, 4, 4, 4], 4, [3, 5]),
        ([1, 2, 3, 4, 5], 3, [2, 2]),
        ([-5, -3, -3, -3, 0, 2, 2, 7], -3, [1, 3]),
        ([1, 2, 3, 4, 5], 0, [-1, -1]),
        ([1, 2, 3, 4, 5], 6, [-1, -1]),
        ([1, 1, 1, 2, 2, 3, 3, 3], 2, [3, 4]),
        ([1, 2, 2, 2, 3, 4], 2, [1, 3]),
        ([1, 1, 1, 1, 1, 1], 1, [0, 5]),
    ]

    for index, (nums, target, expected) in enumerate(tests, start=1):
        result = solution.searchRange(nums, target)
        print(f"测试 {index}：nums={nums}，target={target}，结果={result}，预期={expected}")
        assert result == expected, f"测试 {index} 失败：{result} != {expected}"

    print(f"全部 {len(tests)} 组测试通过！")
