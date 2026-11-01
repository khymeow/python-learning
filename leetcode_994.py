"""
LeetCode 994：腐烂的橘子
英文名称：Rotting Oranges
难度：Medium
题目地址：https://leetcode.cn/problems/rotting-oranges/
核心知识点：二维网格、多源 BFS、deque、坐标与时间元组、新鲜橘子计数。

题目：给定 m×n 网格，0 表示空格，1 表示新鲜橘子，2 表示腐烂橘子。
每分钟所有腐烂橘子同时腐烂上下左右相邻的新鲜橘子。
返回全部橘子腐烂的最少分钟数；无法全部腐烂时返回 -1。

解题思路：多源广度优先搜索（BFS）
1. 遍历整个网格，将全部初始腐烂橘子以 (i, j, 0) 加入同一个队列，
   同时用 fresh 统计新鲜橘子数量；若没有新鲜橘子，直接返回 0。
2. 每次出队得到坐标与时间，检查上下左右四个方向。
3. 仅感染行列索引合法且值为 1 的格子；原地将其标为 2，再令 fresh 减 1。
   入队前完成标记，可防止同一个橘子被重复感染和入队，无须另设 visited。
4. 将 (新坐标, time + 1) 入队。所有源点同时从时间 0 出发，
   BFS 按时间先后处理传播；fresh 降为 0 时立即返回当前感染时间。
5. 队列耗尽仍有新鲜橘子，则返回 -1。本方法会原地修改 grid。

复杂度分析：设网格有 m 行、n 列。
时间复杂度：O(mn)。初始化扫描一次，每个橘子最多入队、出队一次，
每次出队只检查固定的四个方向，fresh 的更新与判断为 O(1)。
空间复杂度：O(mn)。最坏情况下队列需要保存这一数量级的橘子位置与时间。

本次真实学习过程复盘（以下问题均已修正）：
1. 最初用 range(3) 遍历示例网格，并对 range(2)、range(3) 的取值有疑问。
   range(3) 依次取 0、1、2；应通过 len(grid) 和 len(grid[0]) 适配行列数。
2. 行索引必须满足 0 <= ni < len(grid)，不能写成 <= len(grid)，列同理。
3. if 1 not in grid 只检查外层列表元素，不能判断各行中是否还有新鲜橘子。
4. 第一版 all(1 not in row for row in grid) 逻辑正确，但每次感染后
   都重新检查整个网格，产生重复工作；这不是错误解法。
5. 最终改为初始统计 fresh，每感染一个新鲜橘子就 fresh -= 1，
   fresh == 0 时立即返回，避免反复扫描网格。
6. 借鉴第 752 题的 BFS 距离记录，队列保存 (i, j, time) 并进行元组解包。
7. 全部初始腐烂橘子都以时间 0 入队，形成多源 BFS，模拟同时传播。
8. 练习中还讨论了 ()、[]、{}、元组解包、集合成员判断、队列与集合的区别，
   以及 continue 跳过本轮迭代、break 结束所在循环的含义。
"""

from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        fresh = 0

        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))
                elif grid[i][j] == 1:
                    fresh += 1

        if fresh == 0:
            return 0

        while queue:
            i, j, time = queue.popleft()

            for di, dj in directions:
                ni = i + di
                nj = j + dj

                if (0 <= ni < len(grid) and
                    0 <= nj < len(grid[0]) and
                    grid[ni][nj] == 1):

                    grid[ni][nj] = 2
                    fresh -= 1
                    newtime = time + 1
                    queue.append((ni, nj, newtime))

                    if fresh == 0:
                        return newtime

        return -1


if __name__ == "__main__":
    tests = [
        ([[2, 1, 1], [1, 1, 0], [0, 1, 1]], 4),
        ([[2, 1, 1], [0, 1, 1], [1, 0, 1]], -1),
        ([[0, 2]], 0),
        ([[1]], -1),
        ([[0]], 0),
        ([[2, 2], [1, 1]], 1),
        ([[1, 2], [2, 1]], 1),
    ]

    for grid, expected in tests:
        solution = Solution()
        # 解法会原地修改网格，复制每一行以保留测试输入记录。
        test_grid = [row[:] for row in grid]
        result = solution.orangesRotting(test_grid)
        print(f"输入：{grid}，结果：{result}，预期：{expected}")
        assert result == expected

    print("全部 7 组测试通过！")
