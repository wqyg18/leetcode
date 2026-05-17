#
# @lc app=leetcode.cn id=241 lang=python3
#
# [241] 为运算表达式设计优先级
#
from typing import List


# @lc code=start
class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        # 每遇到一个运算符, 就拆分成左右, 然后递归计算所有的可能

        # dfs return 表达式 expr 在所有可能加括号方式下，能计算出的所有结果
        def dfs(expr):
            res = []

            for i, ch in enumerate(expr):
                if ch in "+-*":
                    # 这里拆分的意思是, 把当前这个符号, 当做最后一步计算
                    # 那么需要知道左边可以有哪些值, 右边可以有哪些值
                    left_vals = dfs(expr[:i])
                    right_vals = dfs(expr[i + 1 :])

                    # 对于左边右边所有的取值, 直接eval计算
                    for a in left_vals:
                        for b in right_vals:
                            res.append(eval(f"{a}" + ch + f"{b}"))

            # 如果 res 还是空，说明 expr 里面没有运算符，是纯数字
            # 这里就是dfs的退出, 因为dfs到最后一层, 肯定都是纯数字, 然后退回到上一层, 进行eval
            if not res:
                return [int(expr)]

            return res

        return dfs(expression)


# @lc code=end
sol = Solution()
res = sol.diffWaysToCompute("2*3-4*5")
print(res)
