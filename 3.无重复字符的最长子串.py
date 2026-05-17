#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#


# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        lookup = set()
        res = 0
        left = 0
        for right in range(len(s)):

            while s[right] in lookup:
                lookup.remove(s[left])
                left += 1

            lookup.add(s[right])
            res = max(res, len(lookup))

        return res


# @lc code=end
sol = Solution()
print(sol.lengthOfLongestSubstring("aab"))
