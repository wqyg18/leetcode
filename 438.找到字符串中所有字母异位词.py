#
# @lc app=leetcode.cn id=438 lang=python3
#
# [438] 找到字符串中所有字母异位词
#
from typing import List
from collections import Counter, defaultdict


# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        count = Counter(p)
        windows = defaultdict(int)
        res = []

        left = 0

        for right in range(len(s)):
            windows[s[right]] += 1

            if right - left + 1 > len(p):
                windows[s[left]] -= 1
                left += 1

            if right - left + 1 == len(p):
                flag = True
                for item, freq in count.items():
                    if windows[item] != freq:
                        flag = False
                        break

                if flag:
                    res.append(left)

        return res


# @lc code=end
sol = Solution()
res = sol.findAnagrams("cbaebabacd", "abc")
print(res)
