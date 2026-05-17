#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#
from typing import List
from collections import defaultdict


# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:        
        # 带有默认值的dict, 传入`list`,即每一个key对应的初始值为`[]`
        res_map = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for char in s:
                count[ord(char) - ord('a')] += 1

            res_map[tuple(count)].append(s)

        return list(res_map.values())

# @lc code=end
sol = Solution()
res = sol.groupAnagrams(
    [
        "eat",
        "tea",
        "tan",
        "ate",
        "nat",
        "bat",
        "ac",
        "bd",
        "aac",
        "bbd",
        "aacc",
        "bbdd",
        "acc",
        "bdd",
    ]
)
print(res)
