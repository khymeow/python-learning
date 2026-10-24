"""
LeetCode 11：盛最多水的容器
难度：Medium

题目：选择两条垂直线，与横轴组成能容纳最多水的容器。

解题思路：双指针
1. 左右指针从数组两端开始，计算当前容器面积并更新最大值。
2. 面积由两指针的距离和较短的高度决定。
3. 向内移动较短一侧的指针，寻找可能更大的面积；等高时移动右指针。

时间复杂度：O(n)
额外空间复杂度：O(1)
"""


def max_area(height):
    left = 0
    right = len(height) - 1
    water = 0

    while left < right:
        water = max(
            (right - left) * min(height[left], height[right]),
            water
        )

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return water


if __name__ == "__main__":
    print(max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]))  # 49
    print(max_area([1, 1]))                       # 1
    print(max_area([4, 3, 2, 1, 4]))              # 16
    print(max_area([1, 2, 1]))                    # 2
    print(max_area([2, 2, 2, 2]))                 # 6
    print(max_area([1, 2, 3, 4, 5]))              # 6
    print(max_area([5, 4, 3, 2, 1]))              # 6
    print(max_area([0, 2, 0, 4, 0, 3, 0]))        # 8
    print(max_area([1, 100, 1, 1, 100, 1]))       # 300
    print(max_area([2, 3, 4, 5, 18, 17, 6]))      # 17
