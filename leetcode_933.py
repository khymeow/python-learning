"""
LeetCode 933：最近的请求次数
难度：Easy
核心知识点：队列、collections.deque、滑动时间窗口。

题目：实现 RecentCounter，统计最近 3000 毫秒内的请求次数。
每次 ping(t) 记录时间为 t 的请求，返回闭区间 [t - 3000, t] 内的请求数。
题目保证每次调用的时间戳 t 严格递增。

解题思路：
1. 在 __init__() 中初始化队列，同一实例的多次 ping() 调用共享该队列。
2. 每次 ping(t) 先将当前时间戳加入队尾。
3. 使用 while 持续移除队首小于 t - 3000 的过期请求。
4. 返回队列长度，即当前时间窗口中的有效请求数量。

使用 deque 的原因：
deque 的 append() 和 popleft() 都支持 O(1) 的端点操作。
列表的 pop(0) 则需要移动后续元素，单次删除的时间复杂度为 O(n)。

边界条件：
统计区间包含两端，因此必须使用 self.queue[0] < t - 3000。
若使用 <=，会错误移除恰好位于左边界的有效请求。

复杂度分析：
单次 ping() 的均摊时间复杂度为 O(1)。一次调用可能移除多个过期请求，
若移除 k 个，则该次调用耗时 O(k + 1)，最坏情况不能直接写为 O(1)。
每个请求最多入队一次、出队一次，因此 m 次调用的总处理成本为 O(m)。
额外空间复杂度：O(n)，其中 n 为队列中保留的有效请求数量。
"""

import collections


class RecentCounter:
    """使用 deque 保存最近时间窗口内的请求时间戳。"""

    def __init__(self):
        self.queue = collections.deque()

    def ping(self, t: int) -> int:
        # 添加当前请求
        self.queue.append(t)

        # 移除超出最近 3000 毫秒范围的请求
        # 统计区间为 [t - 3000, t]，包含两端
        while self.queue[0] < t - 3000:
            self.queue.popleft()

        # 返回有效请求数量
        return len(self.queue)


if __name__ == "__main__":
    rc = RecentCounter()

    print(rc.ping(1))      # 预期：1
    print(rc.ping(100))    # 预期：2
    print(rc.ping(3001))   # 预期：3
    print(rc.ping(3002))   # 预期：3
