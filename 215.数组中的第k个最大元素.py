#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
#
from typing import List
import heapq
# @lc code=start
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for i in range(len(nums)):
            if len(heap) < k:
                heapq.heappush(heap,nums[i])
            elif nums[i] > heap[0]:
                heapq.heapreplace(heap, nums[i])
        
        return heap[0]
# @lc code=end

