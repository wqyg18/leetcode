#
# @lc app=leetcode.cn id=417 lang=python3
#
# [417] 太平洋大西洋水流问题
#
from typing import List


# @lc code=start
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # 反向思考, 看水能淹到哪些地方
        m, n = len(heights), len(heights[0])
        pacific = [[False] * n for _ in range(m)]
        atlantic = [[False] * n for _ in range(m)]

        # 依旧使用方向
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # 依旧dfs, 并且太平洋和大西洋分两次去做
        def dfs(i, j, visited):
            # i,j是能够出发的点
            visited[i][j] = True

            for dx, dy in dirs:
                # 这里比较好的一种处理方式是
                # 跳过所有的不需要处理的情况
                x, y = i + dx, j + dy

                if x < 0 or x >= m or y < 0 or y >= n:
                    continue

                if visited[x][y]:
                    continue

                # 注意是反过来的
                if heights[x][y] < heights[i][j]:
                    continue

                visited[x][y] = True

                dfs(x, y, visited)

        # 太平洋
        for i in range(m):
            pacific[i][0] = True
            dfs(i, 0, pacific)
        for j in range(n):
            pacific[0][j] = True
            dfs(0, j, pacific)

        # 大西洋
        for i in range(m):
            atlantic[i][n - 1] = True
            dfs(i, n - 1, atlantic)
        for j in range(n):
            atlantic[m - 1][j] = True
            dfs(m - 1, j, atlantic)

        res = []
        for i in range(m):
            for j in range(n):
                if pacific[i][j] and atlantic[i][j]:
                    res.append([i, j])

        return res


# @lc code=end
sol = Solution()
res = sol.pacificAtlantic(
    heights=[
        [1, 2, 2, 3, 5],
        [3, 2, 3, 4, 4],
        [2, 4, 5, 3, 1],
        [6, 7, 1, 4, 5],
        [5, 1, 1, 2, 4],
    ]
)
print(res)
