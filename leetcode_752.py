"""
LeetCode 752：打开转盘锁
英文名称：Open the Lock
难度：Medium
题目地址：https://leetcode.cn/problems/open-the-lock/
核心知识点：BFS 最短路径、deque、set、tuple。

题目：从 "0000" 出发，每次将一个拨轮向前或向后转动一格，
避开 deadends 中的死亡状态，返回到达 target 的最少转动次数。
若无法到达，返回 -1。

解题思路：单向广度优先搜索（BFS）
1. 将 deadends 转为集合，使用 visited 记录已经发现的状态。
2. 队列中保存 (状态, 距离) 元组，从 ("0000", 0) 开始搜索。
3. 每个状态的 4 个拨轮分别加 1 或减 1，动态生成 8 个相邻状态。
   使用 % 10 处理 9 到 0、0 到 9 的循环，无须提前建立邻接表。
4. 跳过死亡状态和已访问状态；其余状态先标记，再连同距离加入队列。
5. 每次转动的代价都是 1，队列按距离从小到大搜索，首次找到目标即为最短距离。

复杂度分析：
时间复杂度：O(10^4)。四位数字最多有 10^4 个状态，每个状态最多展开一次，
生成 8 个相邻状态；字符串长度固定为 4，集合查询和添加按平均 O(1) 计算。
将死亡列表转为集合另需 O(D) 时间，D 为其长度；题目中 D 至多 500，
因此总体仍写为 O(10^4)。
空间复杂度：O(10^4)。队列和 visited 最多保存这一数量级的状态，
死亡集合及每次临时生成的 8 个相邻状态不改变该数量级。

本次学习记录：
1. deque("0000") 会将字符串拆成 4 个字符；deque(["0000"]) 则只有
   一个完整状态。本题还需距离，因此使用 deque([("0000", 0)])。
2. append() 添加一个整体，extend() 逐个添加可迭代对象中的元素。
   queue.append((neighbor, distance + 1)) 将元组作为一个队列元素，
   换成 extend() 会把状态和距离拆开，破坏队列元素结构。
3. set("0000") 得到 {"0"}；{"0000"} 保存的是完整的四位状态。
4. state, distance = queue.popleft() 将取出的二元组拆包为状态与距离。
5. 队列同时记录距离，才能在生成下一步时用 distance + 1 返回最少转动次数；
   visited 只负责防止重复搜索，不能单独提供距离。
6. 先排除起点死亡，再判断是否已经到达目标，否则当起点与目标都是 "0000"
   且起点死亡时，会误返回 0。目标为其他死亡状态时也应返回 -1。
7. 使用 set 进行死亡状态与访问状态的成员判断，平均 O(1)，
   避免在每次生成邻居时都线性扫描列表。
"""

from collections import deque
from typing import List


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def get_neighbors(state):
            neighbors = []

            for i in range(len(state)):
                digit = int(state[i])

                for change in (1, -1):
                    new_digit = (digit + change) % 10
                    new_state = state[:i] + str(new_digit) + state[i + 1:]
                    neighbors.append(new_state)

            return neighbors

        deadends = set(deadends)
        visited = {"0000"}
        queue = deque([("0000", 0)])

        if "0000" in deadends:
            return -1
        elif target == "0000":
            return 0
        elif target in deadends:
            return -1

        while queue:
            state, distance = queue.popleft()

            for neighbor in get_neighbors(state):
                if neighbor not in visited and neighbor not in deadends:
                    if neighbor == target:
                        return distance + 1

                    visited.add(neighbor)
                    queue.append((neighbor, distance + 1))

        return -1


if __name__ == "__main__":
    solution = Solution()
    tests = [
        (["0201", "0101", "0102", "1212", "2002"], "0202", 6),
        (["8888"], "0009", 1),
        (["0000"], "8888", -1),
        ([], "0000", 0),
        (["0001"], "0001", -1),
    ]

    for deadends, target, expected in tests:
        result = solution.openLock(deadends, target)
        print(f"死亡状态：{deadends}，目标：{target}，结果：{result}，预期：{expected}")
        assert result == expected

    print("全部 5 组测试通过！")
