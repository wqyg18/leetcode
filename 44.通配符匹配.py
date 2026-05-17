#
# @lc app=leetcode.cn id=44 lang=python3
#
# [44] 通配符匹配
#


# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)

        dp = [[False] * (n + 1) for _ in range(m + 1)]

        dp[0][0] = True
        # 初始化
        # p是空字符串显然无法匹配
        # s是空字符串，那么要求p中只能包含"*"
        for j in range(1, n + 1):
            dp[0][j] = dp[0][j - 1] and p[j - 1] == "*"

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == "?" or p[j - 1] == s[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == "*":
                    # 此时匹配0个字符 或者 匹配1个或多个字符
                    # 对于匹配0个字符, 那么当然就是dp[i][j - 1]
                    # 对于后者, 那么就是, 现在"*"匹配了, 最后一个, 那么看剩下的能不能匹配
                    # 这里不需要一直while往前判断, 因为上一轮的i, 在遍历到这个j的时候, 已经做了这个事情了
                    # dp[0][j] -> dp[1][j] -> dp[2][j] -> dp[3][j]
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]

                else:
                    dp[i][j] = False

        return dp[m][n]


# @lc code=end
sol = Solution()
res = sol.isMatch(s="aa", p="*")
print(res)
