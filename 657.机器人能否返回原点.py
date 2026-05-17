#
# @lc app=leetcode.cn id=657 lang=python3
#
# [657] 机器人能否返回原点
#


# @lc code=start
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        pos = [0, 0]
        for move in moves:
            if move == "R":
                pos[0] += 1
            elif move == "L":
                pos[0] += -1
            elif move == "U":
                pos[1] += 1
            elif move == "D":
                pos[1] += -1

        return pos == [0, 0]


# @lc code=end
sol = Solution()
res = sol.judgeCircle(moves="LL")
print(res)
