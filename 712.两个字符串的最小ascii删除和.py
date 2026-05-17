#
# @lc app=leetcode.cn id=712 lang=python3
#
# [712] 两个字符串的最小ASCII删除和
#


# @lc code=start
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        l1, l2 = len(s1), len(s2)

        dp = [[float("inf")] * (l2 + 1) for _ in range(l1 + 1)]  # 1-based
        # dp[i][j]: s1[:i] and s2[:j] 相等所需要的结果
        dp[0][0] = 0
        # 因为我们遍历的时候,从1开始, 所以如果0对应的状态是有意义的, 需要正确初始化
        # 因为后面不会遍历到dp[i][0]和dp[0][i], 但是会用到

        for i in range(1, l1 + 1):
            dp[i][0] = dp[i - 1][0] + ord(s1[i - 1])

        for j in range(1, l2 + 1):
            dp[0][j] = dp[0][j - 1] + ord(s2[j - 1])

        for i in range(1, l1 + 1):
            for j in range(1, l2 + 1):
                char1 = s1[i - 1]
                char2 = s2[j - 1]
                if char1 == char2:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    # 不相等那么对应三种情况, 都删了, 只删char1, 只删char2
                    dp[i][j] = min(
                        dp[i - 1][j - 1] + ord(char1) + ord(char2),
                        dp[i - 1][j] + ord(char1),
                        dp[i][j - 1] + ord(char2),
                    )

        return dp[l1][l2]


# @lc code=end
sol = Solution()
res = sol.minimumDeleteSum(s1="sea", s2="eat")
print(res)
