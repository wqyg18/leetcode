#
# @lc app=leetcode.cn id=96 lang=python3
#
# [96] 不同的二叉搜索树
#


# @lc code=start
class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1

        for i in range(1, n + 1):
            # 枚举root节点
            for root in range(1, i + 1):
                left_count = root - 1
                right_count = i - root

                dp[i] += dp[left_count] * dp[right_count]
        
        return dp[n]


# @lc code=end
sol = Solution()
res = sol.numTrees(n = 3)
print(res)