#
# @lc app=leetcode.cn id=2140 lang=python3
#
# [2140] 解决智力问题
#
from typing import List


# @lc code=start
class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * (n + 1)
        # dp[i]: 从第 i 题开始往后，最多可以拿多少分
        dp[n] = 0
        # 这题倒序比较好处理
        # 因为涉及到了i + 1所以从n-1开始遍历, 这和正序从1开始遍历是一致的
        for i in range(n - 1, -1, -1):
            points, brainpower = questions[i]

            # 不做第 i 题
            skip = dp[i + 1]

            # 做第 i 题
            next_i = i + brainpower + 1
            take = points
            if next_i < n:
                take += dp[next_i]

            dp[i] = max(skip, take)

        return dp[0]


# @lc code=end
sol = Solution()
res = sol.mostPoints(questions=[[12,46],[78,19],[63,15],[79,62],[13,10]]
)
print(res)
