#
# @lc app=leetcode.cn id=994 lang=python3
#
# [994] 腐烂的橘子
#
from typing import List
from collections import deque


# @lc code=start
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # 要求解的是， 最小分钟数， 那么不能直接照搬岛屿数量的解法
        # 这题也不是dfs， 而是bfs

        # 找到所有的腐烂橘子， 然后开始一圈一圈扩散

        m, n = len(grid), len(grid[0])
        queue = deque()
        fresh = 0

        # 收集最初的所有腐烂橘子, 以及统计新鲜橘子的数量
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1

        if fresh == 0:
            return 0

        miutes = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # BFS 开始一层一层腐烂
        while queue and fresh > 0:
            # 这里需要先统计一下当前queue的数量, 因为下面会append
            size = len(queue)

            for _ in range(size):
                i, j = queue.popleft()

                for dx, dy in directions:
                    x, y = i + dx, j + dy
                    # 判断边界, x,y必须是合理下标
                    if x < 0 or x >= m or y < 0 or y >= n:
                        continue

                    # 接下来只会处理fresh的情况
                    if grid[x][y] != 1:
                        continue

                    # 当前x,y肯定是新鲜橘子, 那么需要腐烂, 然后加到下一轮中
                    grid[x][y] = 2
                    fresh -= 1
                    queue.append((x, y))

                    # 最后之所以没有再次queue.append((i, j)), 是因为, 当前(i, j)已经周围一圈的全部腐烂了
                    # 所以直接用周围一圈的就可以了，当然也可以加进来， 不过会空转很多次
            miutes += 1

        return miutes if fresh == 0 else -1


# @lc code=end
sol = Solution()
res = sol.orangesRotting(grid=[[2, 1, 1], [1, 1, 0], [0, 1, 1]])
print(res)
