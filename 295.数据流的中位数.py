#
# @lc app=leetcode.cn id=295 lang=python3
#
# [295] 数据流的中位数
#
import heapq


# @lc code=start
class MedianFinder:

    def __init__(self):
        self.count = 0

        self.min_heap = []
        self.max_heap = []

    def addNum(self, num: int) -> None:
        self.count += 1

        heapq.heappush(self.max_heap, -1 * num)
        heapq.heappush(self.min_heap, -1 * heapq.heappop(self.max_heap))

        if len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -1 * heapq.heappop(self.min_heap))

    def findMedian(self) -> float:
        # 题目保证了至少有一个元素

        # 奇数
        if self.count % 2 == 1:

            return (
                self.min_heap[0]
                if len(self.min_heap) > len(self.max_heap)
                else -1 * self.max_heap[0]
            )
        # 偶数
        else:
            return (self.min_heap[0] - self.max_heap[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end
