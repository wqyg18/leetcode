#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 找出字符串中第一个匹配项的下标
#


# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        for fast in range(len(haystack) - len(needle) + 1):
            slow = 0
            while slow < len(needle) and haystack[fast + slow] == needle[slow]:
                slow += 1

            if slow == len(needle):
                return fast

        return -1


# @lc code=end
sol = Solution()
res = sol.strStr("abc", "c")
print(res)
