#
# @lc app=leetcode.cn id=91 lang=python3
#
# [91] 解码方法
#


# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
        # 没办法用backtracking, 因为是要两位去解码, 还要判断是不是<=26

        dp = [0] * (len(s) + 1)
        # dp[i] : s[:i]对应的解码数
        # dp[0] = 1是一种方案
        # dp[0] = 1是有意义的, 所以dp初始化为len(s) + 1个

        if s[0] == "0":
            return 0
        dp[0] = 1
        dp[1] = 1

        for i in range(2, len(s) + 1):
            # 看s[i-1]能不能单独解码
            # 以及s[i-1] + s[i-1]能不能组合解码


            # 只有两种情况, 1: 单独解码 2: 和前一位组合解码
            if s[i - 1] != "0":
                dp[i] += dp[i - 1]
            if 10 <= int(s[i - 2] + s[i - 1]) <= 26:
                dp[i] += dp[i - 2]

        return dp[len(s)]


# @lc code=end
sol = Solution()
res = sol.numDecodings("10")
print(res)
