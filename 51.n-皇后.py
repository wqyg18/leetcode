#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N 皇后
#
from typing import List


# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # 暴力枚举 但是剪枝

        # 每行放一个, 然后开始遍历每一列是否可以防止(不同列, 不同斜线)
        # 不同列: 列不相等
        # 不同斜线: abs(行差) != abs(列差)
        res = []
        path = []
        cols = set()
        diag1 = set()
        diag2 = set()

        def backtrack(row):
            # 遍历到最后一行, 证明当前方案可行, 保存一次
            if row == n:
                # path[:]是为了复制结果,而不是复制引用,因为path一直在被修改
                res.append(path[:])
                return

            for col in range(n):
                
                if col in cols or row - col in diag1 or row + col in diag2:
                    continue

                # 当前col可以放
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)

                row_str = "." * col + "Q" + "." * (n - col - 1)
                path.append(row_str)

                # 当前列的这一行遍历放好了,开始递归下一行, 直到n
                backtrack(row + 1)

                # 运行到这里证明递归完了一轮, 需要更新重置path,cols,diag1,diag2
                # 此时path中存放的是n个格子对应的一种放置方法
                path.pop()
                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)

        backtrack(0)
        return res


# @lc code=end
sol = Solution()
res = sol.solveNQueens(4)
print(res)
