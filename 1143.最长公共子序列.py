#
# @lc app=leetcode.cn id=1143 lang=python3
#
# [1143] 最长公共子序列
#


# @lc code=start
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)

        dp = [[0] * (m + 1) for _ in range(n + 1)]
        # dp[i][j]: text1[0:i] and text[0:j] 的最长子序列的长度
        # 0...i-1,  0...j-1
        dp[0][0] = 0

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    # 如果text1[i - 1] != text2[j - 1]
                    # 那么尝试丢掉text1[i - 1]或者text2[j - 1]再对比剩下的
                    # 取两者的最大值
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[n][m]


# @lc code=end
sol = Solution()
res = sol.longestCommonSubsequence(text1 = "abc", text2 = "def")
print(res)
