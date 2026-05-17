#
# @lc app=leetcode.cn id=139 lang=python3
#
# [139] 单词拆分
#
from typing import List


# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # 可以多次使用, 显然是一个完全背包, 正序遍历

        # dp[i] s[0:i]是否可以被表示出来
        dp = [False] * (len(s) + 1)
        # 0, 即什么都没有, 显然可以表示出来
        dp[0] = True

        for i in range(1, len(s) + 1):
            for word in wordDict:
                # 现在遍历到i, 那么应该检查, 基于i往前推len(word), 是否是相等的
                if word == s[i - len(word) : i]:
                    dp[i] = dp[i] or dp[i - len(word)]

        return dp[len(s)]


# @lc code=end
sol = Solution()
res = sol.wordBreak(s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"])
print(res)
