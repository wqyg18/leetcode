#
# @lc app=leetcode.cn id=733 lang=python3
#
# [733] 图像渲染
#
from typing import List


# @lc code=start
class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        # 就是找到(sr,sc)的岛屿, 注意需要是和image[sr][sc]数值一致

        # 如果原始的和color一样, 直接返回

        def dfs(i, j, target):
            if i < 0 or i >= len(image):
                return
            if j < 0 or j >= len(image[0]):
                return

            if image[i][j] != target:
                return

            # 开始处理
            image[i][j] = color

            dfs(i - 1, j, target)
            dfs(i + 1, j, target)
            dfs(i, j - 1, target)
            dfs(i, j + 1, target)

        if color == image[sr][sc]:
            return image
        dfs(sr, sc, image[sr][sc])
        return image


# @lc code=end
sol = Solution()
res = sol.floodFill(image=[[0, 0, 0], [0, 0, 0]], sr=0, sc=0, color=0)
print(res)
