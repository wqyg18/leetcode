#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#


# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 中心扩展, 对于奇数和偶数分别处理
        def expand(left: int, right: int) -> str:
            while left >= 0 and right <= len(s) - 1 and s[left] == s[right]:
                left -= 1
                right += 1
            # 注意最后的left和right均不应该取到
            return s[left + 1 : right]

        res = ""

        for i in range(len(s)):

            # 偶数, [i,i+1]为中心
            even_s = expand(i, i + 1)
            # 奇数, [i]为中心
            odd_s = expand(i, i)

            res = even_s if len(even_s) > len(res) else res
            res = odd_s if len(odd_s) > len(res) else res

        return res


# @lc code=end
sol = Solution()
res = sol.longestPalindrome("babad")
print(res)
