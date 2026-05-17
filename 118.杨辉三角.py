#
# @lc app=leetcode.cn id=118 lang=python3
#
# [118] 杨辉三角
#
from typing import List


# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]

        dp = [[] for _ in range(numRows)]
        dp[0] = [1]
        dp[1] = [1, 1]
        
        for i in range(2,numRows):
            dp[i] = [1] * (i + 1)
            for j in range(1, len(dp[i - 1])):
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]

        return dp


# @lc code=end
sol = Solution()
res = sol.generate(3)
print(res)