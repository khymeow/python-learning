"""
LeetCode 695：岛屿的最大面积（Max Area of Island）
难度：Medium
题目：https://leetcode.cn/problems/max-area-of-island/

一、题目描述
给定一个由整数 0（水）和 1（陆地）组成的二维网格 grid。
上下左右相邻的陆地属于同一座岛屿，对角线相邻不算连通。
岛屿面积是组成这座岛屿的陆地格子数量。
返回最大岛屿的面积；如果不存在岛屿，返回 0。

二、自己的解题思路（递归 DFS）
1. 使用外层两层 for 遍历每一个格子，寻找未访问的陆地作为新岛屿的起点。
2. 用 visited 集合记录已经访问过的坐标，避免重复搜索。
3. 定义 dfs(i, j)，使用 num = 1 计算当前格子贡献的面积。
4. 遍历上下左右四个方向：若邻居在边界内、未访问且为陆地，就先标记，再递归。
5. 使用 num += dfs(ni, nj) 把递归分支返回的面积累加到当前面积。
6. 每完成一座岛屿的搜索，就用 maxarea = max(maxarea, dfs(i, j)) 更新最大面积。

三、本次实际遇到的问题与修正
1. 变量名沿用上一道图像渲染题：
   错误：if image[ni][nj] == 1:
   修正：if grid[ni][nj] == 1:
   原因：本题输入变量名是 grid，不是 image。

2. 外层最大面积变量未初始化：
   早期版本在外层写过 num = max(num, dfs(i, j))，但外层 num 尚未定义。
   修正：初始化 maxarea = 0，使用 maxarea = max(maxarea, dfs(i, j))。
   注意：dfs 内部的 num 是局部变量，与外层变量不是同一个。

3. 忽略递归函数的返回值：
   错误写法：
       num += 1
       dfs(ni, nj)
   修正写法：
       num += dfs(ni, nj)
   原因：dfs 自身以 num = 1 统计当前格子，需要把子递归返回的整片面积累加回来。
   只执行 dfs 而不使用其返回值，会遗漏更深层陆地的面积。

4. 外层启动 DFS 时未检查 visited：
   早期条件：if grid[i][j] == 1:
   修正：if grid[i][j] == 1 and (i, j) not in visited:
   原因：一座岛屿应只启动一次完整 DFS，不必从已访问陆地重复搜索。

5. 测试用例曾有预期值错误（属于测试数据问题，不是本题代码错误）：
   [[1, 0, 0], [1, 0, 1], [1, 0, 1]] 的最大岛屿面积应为 3，而不是 2。
   左侧一列有 3 块相连陆地。

四、复杂度分析
设网格有 m 行、n 列：
- 时间复杂度：O(mn)。每个格子被外层检查一次，每块陆地最多进入 DFS 一次。
- 额外空间复杂度：O(mn)。visited 和递归调用栈在最坏情况下均可达到 O(mn)。

五、学习注意事项
- 本题与 LeetCode 733 的区别：733 主要是“递归执行操作”；695 要“递归计算并返回结果”。
- 当前方法保留了自己写的 visited 集合，不改成原地修改网格的其他写法。
- Python 的递归深度有限：对很大的连续陆地，递归 DFS 可能触发 RecursionError。
  理论复杂度正确并不代表递归实现能通过所有极端规模输入；遇到该问题可考虑显式栈 DFS 或 BFS。

代码学习记录：最终 DFS 实现由自己编写，在调试过程中根据问题讲解修正了上述错误。
"""

from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]
        visited = set()
        maxarea = 0

        def dfs(i, j):
            num = 1
            for di, dj in directions:
                ni = i + di
                nj = j + dj
                if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]) and (ni, nj) not in visited:
                    if grid[ni][nj] == 1:
                        visited.add((ni, nj))
                        num += dfs(ni, nj)
            return num

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i, j) not in visited:
                    visited.add((i, j))
                    maxarea = max(maxarea, dfs(i, j))

        return maxarea


if __name__ == "__main__":
    tests = [
        ([[0, 0], [0, 0]], 0),                    # 全水
        ([[1]], 1),                              # 单格陆地
        ([[0]], 0),                              # 单格水
        ([[1, 1], [1, 1]], 4),                    # 全部连通
        ([[1, 0], [0, 1]], 1),                    # 仅对角线相邻，不连通
        ([[1, 1, 0], [0, 1, 0], [0, 1, 1]], 5),  # 不规则岛屿
        ([[1, 1, 0, 1], [1, 0, 0, 1], [0, 0, 0, 1]], 3),  # 多座岛屿
        ([[1, 0, 1, 0, 1]], 1),                  # 多个独立小岛
        ([[1, 1, 1, 1, 1]], 5),                  # 单行连续陆地
        ([[1, 0, 0], [1, 0, 1], [1, 0, 1]], 3),  # 修正旧测试的错误预期
    ]

    for idx, (grid, expected) in enumerate(tests, 1):
        result = Solution().maxAreaOfIsland(grid)
        assert result == expected, (
            f"测试 {idx} 失败：实际结果 {result}，预期结果 {expected}"
        )
        print(f"测试 {idx}: PASS（结果：{result}）")

    print("全部 10 组测试通过！")
