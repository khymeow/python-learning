"""
LeetCode 1971：寻找图中是否存在路径
英文名称：Find if Path Exists in Graph
难度：Easy
核心知识点：图、邻接表、BFS、队列、集合去重。

题目：给定节点数 n、无向边列表 edges、起点 source 和终点 destination，
节点编号为 0 到 n - 1，判断能否从起点到达终点。
能够到达返回 True，否则返回 False。

解题思路：邻接表加广度优先搜索（BFS）
1. 使用 range(n) 为每个节点创建空的邻居列表。
2. 遍历每条无向边 [a, b]，同时记录 a 到 b 和 b 到 a 两个方向。
3. 用 deque([source]) 初始化队列，用 {source} 初始化已发现集合 visited。
4. 循环取出队首节点；若为终点，则立即返回 True。
5. 遍历当前节点的邻居，先将未发现的邻居加入 visited，再将其加入队列。
6. 队列耗尽后仍未找到终点，则返回 False。

复杂度分析：设节点数为 V，边数为 E。
时间复杂度：O(V + E)。初始化邻接表需要 O(V)，每条无向边记录两次，
建边需要 O(E)。BFS 中每个节点最多入队、出队一次，所有邻接表项最多
被检查一次；无向边共对应 2E 个邻接表项，因此遍历为 O(V + E)。
空间复杂度：O(V + E)。邻接表占 O(V + E)，队列和 visited 各占 O(V)。

本次学习易错点：
1. n 是整数，不能直接写 for i in n；应使用 for i in range(n)。
2. 无向边必须同时执行 graph[a].append(b) 和 graph[b].append(a)。
3. source 是整数，deque(source) 无法初始化；deque([source]) 先创建
   只含起点的列表，再交给 deque 构造队列。
4. 添加元素应调用队列实例的 queue.append(neighbor)，而不是
   对 deque 类直接调用 deque.append(neighbor)。
5. 入队前先执行 visited.add(neighbor)，防止重复入队，避免在环中反复访问。
6. 节点出队后即可检查终点。return True 会立即结束当前函数调用，
   无须等待遍历结束；仅在队列耗尽且未找到终点时返回 False。
"""

from collections import deque


class Solution(object):
    def validPath(self, n, edges, source, destination):
        # 创建邻接表，为每个节点初始化空列表
        graph = {}

        for i in range(n):
            graph[i] = []

        # 建立无向图：每条边都需要记录两个方向
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        # 初始化队列和已访问集合
        queue = deque([source])
        visited = {source}

        # 使用 BFS 搜索
        while queue:
            current = queue.popleft()

            # 找到终点，立即返回
            if current == destination:
                return True

            # 遍历当前节点的所有邻居
            for neighbor in graph[current]:
                if neighbor not in visited:
                    # 先标记已发现，再加入队列
                    visited.add(neighbor)
                    queue.append(neighbor)

        # 所有可达节点搜索完毕，仍未找到终点
        return False


if __name__ == "__main__":
    solution = Solution()

    # 测试 1：存在路径 0 -> 1 -> 2
    assert solution.validPath(3, [[0, 1], [1, 2]], 0, 2) is True

    # 测试 2：两个不连通的部分
    assert solution.validPath(4, [[0, 1], [2, 3]], 0, 3) is False

    # 测试 3：起点与终点相同
    assert solution.validPath(1, [], 0, 0) is True

    # 测试 4：终点是起点的直接邻居
    assert solution.validPath(3, [[0, 1], [1, 2]], 0, 1) is True

    # 测试 5：图中存在环
    assert solution.validPath(3, [[0, 1], [1, 2], [2, 0]], 0, 2) is True

    print("所有测试通过！")
