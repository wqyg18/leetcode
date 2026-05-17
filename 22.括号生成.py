#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#
from typing import List


# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(s, left, right):
            # 先写终止条件
            if len(s) == n * 2:
                res.append(s)
                return

            if left < n:
                backtrack(s + "(", left + 1, right)

            if right < left:
                backtrack(s + ")", left, right + 1)

        backtrack("", 0, 0)

        return res


# @lc code=end
sol = Solution()
res = sol.generateParenthesis(n=3)
print(res)
