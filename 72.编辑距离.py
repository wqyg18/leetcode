#
# @lc app=leetcode.cn id=72 lang=python3
#
# [72] 编辑距离
#


# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]
        # dp[i][j] = word1 的前 i 个字符，变成 word2 的前 j 个字符，最少需要几步
        # 0...i-1, 0...j-1

        dp[0][0] = 0
        for i in range(len(word1) + 1):
            dp[i][0] = i

        for j in range(len(word2) + 1):
            dp[0][j] = j

        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    # 三种操作取最小值
                    dp[i][j] = min(
                        dp[i][j - 1] + 1, # 插入
                        # 先把 word1[:i] 变成 word2[:j-1]，然后插入 word2[j-1]
                        dp[i - 1][j] + 1, # 删除
                        # 先把 word1[:i-1] 变成 word2[:j]，然后删掉多出来的 word1[i-1]
                        dp[i - 1][j - 1] + 1, # 替换
                        # 先把前面的部分变好，然后把 word1[i-1] 替换成 word2[j-1]。
                    )

        return dp[len(word1)][len(word2)]


# @lc code=end
sol = Solution()
res = sol.minDistance(word1="horse", word2="ros")
print(res)
