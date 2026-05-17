#
# @lc app=leetcode.cn id=474 lang=python3
#
# [474] 一和零
#
from typing import List


# @lc code=start
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # 最后得到的子集中,最多m个0, n个1
        # 二维背包问题, 以目标为导向
        # dp[i][j]: 最多i个0,j个1, 对应的子集的最大长度
        # dp = [[0] * (n + 1)] * (m + 1) 这样初始化是引用的, 不行
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # 对于 strs[k], 里面有 k1个0, k2个1
        # 那么加上strs[k]
        # dp[i][j] = max(dp[i][j], dp[i-k1][j-k2] + 1)
        # 含义是, 要么不选这个新的str
        # 要么选的话, 需要腾出来位置

        for s in strs:
            str_zero = s.count("0")
            str_one = s.count("1")

            for i in range(m, str_zero - 1, -1):
                for j in range(n, str_one - 1, -1):
                    # 拿还是不拿s
                    dp[i][j] = max(dp[i][j], dp[i - str_zero][j - str_one] + 1)
        
        return dp[m][n]


# @lc code=end
sol = Solution()
res = sol.findMaxForm(strs = ["10", "0001", "111001", "1", "0"], m = 5, n = 3)
print(res)