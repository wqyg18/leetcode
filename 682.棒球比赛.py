#
# @lc app=leetcode.cn id=682 lang=python3
#
# [682] 棒球比赛
#
from typing import List


# @lc code=start
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = []
        for i in range(len(operations)):
            op = operations[i]
            if op == "+":
                res.append(res[-1] + res[-2])
            elif op == "D":
                res.append(res[-1] * 2)
            elif op == "C":
                res.pop()
            else:
                res.append(int(op))

        return sum(res)


# @lc code=end

sol = Solution()
res = sol.calPoints(operations = ["5","-2","4","C","D","9","+","+"])
print(res)
