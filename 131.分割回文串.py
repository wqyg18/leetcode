#
# @lc app=leetcode.cn id=131 lang=python3
#
# [131] 分割回文串
#
from typing import List


# @lc code=start
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        path = []
        res = []

        def is_palindrome(sub: str) -> bool:
            return sub == sub[::-1]

        def backtrack(start):
            if start == len(s):
                res.append(path[:])
                return
            for i in range(start, len(s)):
                # 从start开始, 看直到i这一部分是不是回文的
                cur = s[start : i + 1]

                if not is_palindrome(cur):
                    continue

                # 如果是回文的, 就加到path中, 然后开始往后递归
                # 递归完成再接着下一个, 所以需要pop
                path.append(cur)
                backtrack(i + 1)
                path.pop()

        backtrack(0)
        return res


# @lc code=end
sol = Solution()
res = sol.partition(s="aab")
print(res)
