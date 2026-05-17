#
# @lc app=leetcode.cn id=1851 lang=python3
#
# [1851] 包含每个查询的最小区间
#
from typing import List
import heapq


# @lc code=start
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:

        intervals.sort(key=lambda x: x[0])
        sorted_queries = sorted((q, i) for i, q in enumerate(queries))

        res = [-1] * len(queries)
        heap = []
        idx = 0

        for q, original_idx in sorted_queries:
            # 把所有 l <= q 的区间加入候选池
            while idx < len(intervals) and intervals[idx][0] <= q:
                l, r = intervals[idx]
                length = r - l + 1
                heapq.heappush(heap, (length, r))
                idx += 1

            # 弹出所有已经过期的区间
            # r < q，说明这个区间已经不可能包含当前 q
            while heap and heap[0][1] < q:
                heapq.heappop(heap)

            # 堆顶就是当前 q 能使用的最短区间
            # 可以重复使用, 所以不需要pop, 直接取堆顶值
            if heap:
                res[original_idx] = heap[0][0]

        return res


# @lc code=end
sol = Solution()
res = sol.minInterval(
    intervals=[[2, 3], [2, 5], [1, 8], [20, 25]], queries=[2, 19, 5, 22]
)
print(res)
