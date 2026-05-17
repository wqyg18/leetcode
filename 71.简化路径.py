#
# @lc app=leetcode.cn id=71 lang=python3
#
# [71] 简化路径
#


# @lc code=start
class Solution:
    def simplifyPath(self, path: str) -> str:
        parts = path.split("/")
        # split()会按照指定的key分割, 同时结果不会包含分隔符

        stack = []
        # 栈: 栈顶(pop的结果)是当前所在目录
        for part in parts:
            # 当前元素是 "/"
            if part == "":
                continue
            elif part == ".":
                continue
            elif part == "..":
                # 表示需要回到上一级目录
                if len(stack) > 0:  # 栈中有元素, 表示不是根目录
                    stack.pop()
                else:
                    continue
            else:
                stack.append(part)

        return "/" + "/".join(stack)


# @lc code=end

sol = Solution()
res = sol.simplifyPath(path="/home/")
print(res)
