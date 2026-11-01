"""
LeetCode 200：岛屿数量
英文名称：Number of Islands
难度：Medium
题目地址：https://leetcode.cn/problems/number-of-islands/
核心知识点：BFS、二维网格、deque、集合去重、嵌套循环、连通区域计数。

题目：给定由字符 '1'（陆地）和 '0'（水）组成的 m×n 网格，
统计独立岛屿数量。只有上下左右相邻的陆地连通，对角线不算相邻。

最终思路：一次外层遍历加 BFS
1. 外层双重 for 遍历网格，寻找尚未访问的陆地。
2. 将坐标元组加入队列并记录到 visited，启动 while queue 搜索当前岛屿。
3. 使用 x、y 表示出队坐标，与外层 i、j 区分；检查四个方向及合法边界。
4. 对未访问的相邻陆地，入队时立即标记，防止重复入队。
5. 当前岛屿搜索完毕后 num += 1，再回到外层 for 继续寻找新岛屿。
6. 返回 num。使用 visited 记录坐标，不修改输入网格。

初版与优化版：
初版先统计陆地数 onenum，再用 while onenum != 0 反复从左上角寻找
未访问陆地；通过 found 和两次 break 退出两层 for，再执行当前岛屿的 BFS。
初版经修正后逻辑正确，但寻找新起点会重复扫描网格。
设岛屿数为 k，重复扫描的最坏成本为 O(kmn)；k 最多为 O(mn)，
最坏总时间可达 O((mn)^2)，额外空间为 O(mn)。
优化后只保留一次外层遍历，在找到起点时直接执行 BFS，
不再需要 onenum、外围 while、found 和两次 break，核心 BFS 思路不变。

复杂度分析：
时间复杂度：O(mn)。外层扫描每个格子一次，每块陆地最多入队、出队一次，
每次只检查四个方向；集合成员判断与添加按平均 O(1) 计算。
额外空间复杂度：O(mn)。visited 和队列最坏保存这一数量级的坐标。

真实学习过程与错误复盘（以下问题已修正）：
1. 曾把 grid[ni][nj] 与整数 1 比较，但输入是 List[List[str]]，应与 '1'
   比较。1 == '1' 为 False，导致 BFS 无法扩散，将同一岛屿误计为多座。
   这是本次最初实际测试失败的主要原因。
2. 曾写 queue.append(i, j)；append() 只接收一个元素，
   应写为 queue.append((i, j))，将坐标元组整体入队。
3. break 只退出最内层循环；初版使用 found 与第二次 break 才退出两层。
   continue 只跳过所在循环的本轮迭代，return 则结束当前函数调用。
4. 用 set() 创建空集合，用 visited.add((i, j)) 记录已发现坐标。
   队列不会自动去重，必须显式维护 visited；行列索引要严格小于对应长度。
5. 外层 for 与内层 while 分工后，当前岛屿处理结束即可继续扫描，
   消除每找到一座岛屿就重头扫描的重复工作，将 O(kmn) 优化为 O(mn)。

代码来源：最初的 BFS 版本由用户独立编写，经提示完成错误修正；
O(mn) 优化思路经过讲解，最终优化代码由 AI 按用户原代码结构整理。
这不是完全无辅助、一次独立写出的优化版本，后续仍需独立复现。
"""

from collections import deque
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        queue = deque()
        visited = set()

        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]

        num = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):

                if grid[i][j] == '1' and (i, j) not in visited:
                    queue.append((i, j))
                    visited.add((i, j))

                    while queue:
                        x, y = queue.popleft()

                        for di, dj in directions:
                            ni = x + di
                            nj = y + dj

                            if (0 <= ni < len(grid)
                                    and 0 <= nj < len(grid[0])
                                    and (ni, nj) not in visited):

                                if grid[ni][nj] == '1':
                                    queue.append((ni, nj))
                                    visited.add((ni, nj))

                    num += 1

        return num


if __name__ == "__main__":
    tests = [
        ([["1", "1", "1"], ["0", "1", "0"]], 1),
        ([["1", "0"], ["0", "1"]], 2),
        ([["0", "0"], ["0", "0"]], 0),
        ([["1"]], 1),
        ([["0"]], 0),
        ([["1", "0", "1", "0", "1"]], 3),
        ([["1", "1", "0"], ["1", "0", "0"], ["0", "0", "1"]], 2),
        ([["1", "1"], ["1", "1"]], 1),
    ]

    for grid, expected in tests:
        solution = Solution()
        result = solution.numIslands(grid)
        print(f"输入：{grid}，结果：{result}，预期：{expected}")
        assert result == expected

    print("全部 8 组测试通过！")
