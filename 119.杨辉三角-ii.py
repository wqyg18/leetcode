1  #
# @lc app=leetcode.cn id=119 lang=python3
#
# [119] 杨辉三角 II
#
from typing import List


# @lc code=start
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        dp = [[1] * (rowIndex + 1) for _ in range(rowIndex + 1)]

        for i in range(2, rowIndex + 1):
            for j in range(1, i):
                dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]

        return dp[rowIndex]


# @lc code=end
sol = Solution()
res = sol.getRow(0)
print(res)
