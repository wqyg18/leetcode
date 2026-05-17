#
# @lc app=leetcode.cn id=1861 lang=python3
#
# [1861] 旋转盒子
#
from typing import List


# @lc code=start
class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        # 先想用什么去解决
        #

        # 首先每一行应该单独处理, 因为行与行之间是没有关系的
        # 对于每一行来说, 可能障碍物前后都有石头
        # 那么就是, 首先按照障碍物的位置分开处理, 第一段0~第0个障碍物, 然后第0个障碍物~第1个障碍物
        # 第i个障碍物~len(boxGrid[0])

        # 对于每一行, 找到第一个空位置, 然后找到第一个障碍物
        # 如果空在障碍物左边, 那么前面的移动, 然后查找下一个空位, 如果在右边, 那么找下一个障碍物
        # 但是这样不好实现

        m, n = len(boxGrid), len(boxGrid[0])
        for row in boxGrid:
            # 从右往左遍历, 使用一个write指针, 表示未处理的最右侧的石头应该落到的位置
            write = n - 1
            for j in range(n - 1, -1, -1):
                # 障碍物, 那么write只能往左一个
                if row[j] == "*":
                    write = j - 1
                elif row[j] == "#":
                    # 如果是石头, 那么交换位置
                    row[j] = "."
                    row[write] = "#"
                    write = write - 1

        # 最后顺时针转90度
        ans = [["."] * (m) for _ in range(n)]

        for i in range(m):
            for j in range(n):
                ans[j][m - i - 1] = boxGrid[i][j]

        return ans


# @lc code=end
sol = Solution()
res = sol.rotateTheBox(boxGrid=[["#", ".", "#"]])
print(res)
