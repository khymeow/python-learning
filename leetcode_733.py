"""LeetCode 733. 图像渲染 (Flood Fill) — Easy

题目：https://leetcode.cn/problems/flood-fill/

给定二维整数网格 image、起点 (sr, sc) 和新颜色 color，
把与起点通过上下左右连通、且与起点原颜色相同的像素改为新颜色。

解法：递归 DFS（保留学习时完成的实现）。
1. 保存起点的原始颜色 oc；如果原颜色已经是新颜色，直接返回。
2. 从起点递归访问，进入一个格子时立即把它修改成新颜色。
3. 仅对边界内、颜色仍为 oc 的上下左右邻居继续递归。
由于 oc != color，已修改的像素不会再次满足递归条件，
因此无需额外的 visited 集合。

时间复杂度：O(m*n)，最坏遍历全部像素。
额外空间复杂度：O(m*n)，最坏情况下递归调用栈占用 O(m*n)。
注意：图像很大、连通路径很长时，Python 递归深度可能不足。

学习记录：最初用 deque 实现 BFS，随后练习用递归 DFS 重新实现；
检查邻居时需要判断 image[ni][nj] == oc，以免修改不连通或不同色的格子。
"""

from typing import List


class Solution:
    def floodFill(
        self,
        image: List[List[int]],
        sr: int,
        sc: int,
        color: int
    ) -> List[List[int]]:

        oc = image[sr][sc]

        if oc == color:
            return image
        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]

        def dfs(i, j):
            image[i][j]= color
            for di, dj in directions:
                ni = i + di
                nj = j + dj
                if 0 <= ni < len(image) and 0 <= nj < len(image[0]):
                    if image[ni][nj] == oc:
                        dfs(ni,nj)
        dfs(sr,sc)

        return image


if __name__ == "__main__":
    tests = [
        ([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2,
         [[2, 2, 2], [2, 2, 0], [2, 0, 1]]),
        ([[0, 0, 0], [0, 0, 0]], 0, 0, 0,
         [[0, 0, 0], [0, 0, 0]]),
        ([[0, 0, 0], [0, 1, 1]], 1, 1, 2,
         [[0, 0, 0], [0, 2, 2]]),
        ([[1]], 0, 0, 3, [[3]]),
        ([[1, 2], [2, 1]], 0, 0, 9, [[9, 2], [2, 1]]),
        ([[1, 1], [1, 1]], 0, 0, 3, [[3, 3], [3, 3]]),
    ]

    for index, (image, sr, sc, color, expected) in enumerate(tests, start=1):
        actual = Solution().floodFill(image, sr, sc, color)
        assert actual == expected, (
            f"测试 {index} 失败：期望 {expected}，实际 {actual}"
        )
        print(f"测试 {index}: PASS")

    print(f"全部 {len(tests)} 组测试通过")
