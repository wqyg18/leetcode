#
# @lc app=leetcode.cn id=347 lang=python3
#
# [347] 前 K 个高频元素
#
from typing import List
import heapq
from collections import Counter


# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        # heap支持元组, 元组比较规则是字典序
        # 所以要存 (freq, num)

        # 计数
        map = Counter(nums)

        # """
        # 最小堆
        # 找前K大
        for num, freq in map.items():
            if len(heap) < k:
                heapq.heappush(heap, (freq, num))
            elif freq > heap[0][0]:
                heapq.heapreplace(heap, (freq, num))

        return [heap[x][1] for x in range(k)]
        # """

        """
        # 桶排序

        # 创建桶：索引=频率，值=该频率的所有元素
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in map.items():
            buckets[freq].append(num)

        # 收集结果
        result = []
        for freq in range(len(buckets) - 1, 0, -1):
            if buckets[freq]:
                result.extend(buckets[freq])
                if len(result) >= k:
                    # 因为题目数据保证了答案唯一, 不会出现k-1和k+1和k都是一样的频率
                    return result[:k]

        return result
        """


# @lc code=end
