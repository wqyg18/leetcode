#
# @lc app=leetcode.cn id=516 lang=python3
#
# [516] 最长回文子序列
#


# @lc code=start
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        # 回文需要同时关注第一个和最后一个, 所以一维dp不够

        dp = [[0] * (n + 1) for _ in range(n + 2)]
        # 1-based
        # dp[i][j] s[i-1:j]最长回文子序列长度

        for i in range(n, 0, -1):
            for j in range(i, n + 1):
                if s[i - 1] == s[j - 1]:
                    if i != j:
                        dp[i][j] = dp[i + 1][j - 1] + 2
                    else:
                        dp[i][j] = 1
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        return dp[1][n]


# @lc code=end
sol = Solution()
res = sol.longestPalindromeSubseq(s="aaabab")
print(res)
