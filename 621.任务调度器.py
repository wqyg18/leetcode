#
# @lc app=leetcode.cn id=621 lang=python3
#
# [621] 任务调度器
#
from typing import List
from collections import Counter, deque
import heapq


# @lc code=start
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        # 贪心算法
        # 1. 统计每个任务出现的频率 (Frequency)
        counts = Counter(tasks)

        # 2. 找到最高频率 (Max frequency)
        max_f = max(counts.values())

        # 3. 计算有多少个任务达到了这个最高频率 (Number of tasks with max frequency)
        # 例如: A 3次, B 3次, C 2次 -> max_f = 3, max_count = 2 (即A和B)
        max_count = sum(1 for f in counts.values() if f == max_f)

        # 4. 根据公式计算最短时间 (Calculating the result using the formula)
        # 核心逻辑：(max_f - 1) 个完整的周期，每个周期长度为 (n + 1)
        # 最后一个周期只需要放下所有频率为 max_f 的任务即可
        ans = (max_f - 1) * (n + 1) + max_count

        # 5. 与任务总数取最大值 (Handle cases where no idle time is needed)
        # 如果任务种类非常多，填满了所有空位，结果就是任务总数
        return max(ans, len(tasks))
        """

        # 模拟
        print()
        counts = Counter(tasks)

        heap = [(-freq, task) for task, freq in counts.items()]
        heapq.heapify(heap)

        waiting = deque()
        t = 0
        while len(heap) or len(waiting):
            t+=1
            -freq, task = heapq.heappop(heap)
            freq += 1
            if freq != 0:
                waiting.append(-freq, task,t+n)
            if t == 


# @lc code=end
a = [1, 2, 3]
c = Counter(a)
print(list(c.items()))
