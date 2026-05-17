#
# @lc app=leetcode.cn id=981 lang=python3
#
# [981] 基于时间的键值存储
#
from collections import defaultdict


# @lc code=start
class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""
        """
        # 题目规定, timestamp严格递增
        # 从后往前找到小于等于timestamp的最大timestamp_prev
        for t, v in reversed(self.map[key]):
            if t <= timestamp:
                return v
        return ""
        """

        # 二分查找
        # 找到第一个大于timestamp
        nums = self.map[key]
        # [left, right)
        left = 0
        right = len(nums)

        while left < right:
            mid = (left + right) // 2
            if nums[mid][0] <= timestamp:
                left = mid + 1
            else:
                right = mid

        return nums[(left - 1)][1] if left != 0 else ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
# @lc code=end
