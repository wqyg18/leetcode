#
# @lc app=leetcode.cn id=239 lang=python3
#
# [239] 滑动窗口最大值
#
from typing import List
from collections import deque


# @lc code=start
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # 从队列尾部开始遍历, 小于新元素的都踢掉
        # 同时如果队列首元素对应的下标超过了窗口索引, 那么也踢掉
        # 返回队列首元素

        # 队列中只存下标

        queue = deque()
        res = []
        for i in range(len(nums)):
            while (queue) and (nums[queue[-1]] < nums[i]):
                queue.pop()

            queue.append(i)

            # 当前索引边界 [i-k+1 ,i]
            if queue[0] < i - k + 1:
                queue.popleft()

            # 从第k个开始计入结果
            if i >= k-1:
                res.append(nums[queue[0]])

        return res


# @lc code=end
