#
# @lc app=leetcode.cn id=455 lang=python3
#
# [455] 分发饼干
#
from typing import List
# @lc code=start
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # 贪心: 从最小胃口开始, 选择能够满足胃口的最小饼干
        g.sort()
        s.sort()

        i = 0
        j = 0

        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                i += 1
            j += 1
        
        return i
# @lc code=end

