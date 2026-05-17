#
# @lc app=leetcode.cn id=93 lang=python3
#
# [93] 复原 IP 地址
#
from typing import List


# @lc code=start
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        path = []
        res = []

        def backtrack(start):
            if start == len(s) and len(path) == 4:
                res.append(".".join(path[:]))
                return

            # 这里遍历终止条件 使用min(start + 3, len(s)), 是因为, 最大也只能占用3位
            for i in range(start, min(start + 3, len(s))):

                ip = s[start : i + 1]

                # 已经切成四段了, 但是还没有切完
                if len(path) == 4:
                    continue
                # 前导0
                if len(ip) > 1 and ip[0] == "0":
                    continue
                if int(ip) > 255:
                    continue

                path.append(ip)
                backtrack(i + 1)
                path.pop()

        backtrack(0)
        return res


# @lc code=end
sol = Solution()
res = sol.restoreIpAddresses(s="25525511135")
print(res)
