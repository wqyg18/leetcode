#
# @lc app=leetcode.cn id=763 lang=python3
#
# [763] 划分字母区间
#
from typing import List
from collections import Counter


# @lc code=start
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # 首先需要一个counter
        # 从第一个字母开始, 维护一个seen
        # 将第一个字母append到seen, 开始往后遍历, 每遇到一个新字母, 就加到seen中
        # 同时count中的字母-1, 知道seen中对应的字母都为0, 则这是一个片段

        count = Counter(s)
        seen = set()
        start = 0

        res = []
        for i in range(len(s)):
            seen.add(s[i])
            count[s[i]] -= 1

            finish = 0
            for ch in seen:
                if count[ch] == 0:
                    finish += 1
            if finish == len(seen):
                res.append(i - start + 1)
                start = i + 1
                seen = set()

        return res


# @lc code=end
sol = Solution()
res = sol.partitionLabels(s="ababcbacadefegdehijhklij")
print(res)
