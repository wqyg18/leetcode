#
# @lc app=leetcode.cn id=10 lang=python3
#
# [10] 正则表达式匹配
#


# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # 字符串dp
        # 二维dp dp[i][j]: s[:i] and p[:j]是否可以匹配

        m, n = len(s), len(p)

        dp = [[False] * (n + 1) for _ in range(m + 1)]
        # dp[0][j], dp[i][0]后续会用到, 但是没有赋值, 需要初始化
        # 并且注意初始化的时候就应该用到dp的思想了, 不然会浪费
        # 空字符 空字符当然可以匹配
        dp[0][0] = True
        # 显然空字符 和 非空字符串 不能匹配
        for i in range(1, m + 1):
            dp[i][0] = False

        # 初始化的时候注意, 对于"*", 是有可能匹配空字符串的
        # 只有 a*b*c* 这种形式才可能匹配空字符串
        # 遇到"*", 可以直接把前一个字符串消掉
        for j in range(2, n + 1):
            if p[j - 1] == "*":
                dp[0][j] = dp[0][j - 2]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # 因为需要支持"." "*"
                if p[j - 1] == "." or p[j - 1] == s[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == "*":
                    # 情况1：匹配0个前面的字符
                    # 相当于是把"*"前一个字符消掉
                    dp[i][j] = dp[i][j - 2]

                    # 情况2：匹配1个或多个前面的字符
                    # 相当于是看"*"的前一个字符是否可以匹配, 那么就是两种情况,一种是".", 一种是字符匹配
                    if p[j - 2] == "." or p[j - 2] == s[i - 1]:
                        dp[i][j] = dp[i][j] or dp[i - 1][j]
                else:
                    dp[i][j] = False

        return dp[m][n]


# @lc code=end
sol = Solution()
res = sol.isMatch(s="aa", p=".*")
print(res)
