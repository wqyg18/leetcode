#
# @lc app=leetcode.cn id=986 lang=python3
#
# [986] 区间列表的交集
#
from typing import List


# @lc code=start
class Solution:
    def intervalIntersection(
        self, firstList: List[List[int]], secondList: List[List[int]]
    ) -> List[List[int]]:
        # 把B中的区间, 一个一个放到A中, 寻找交集
        # 这样完全是暴力解法

        # 考虑到A,B均是有序列表
        # 可以直接双指针 O(m*n) -> O(m+n)

        i, j = 0, 0
        res = []

        while i < len(firstList) and j < len(secondList):
            start1, end1 = firstList[i]
            start2, end2 = secondList[j]

            # 判断是否有交集
            left = max(start1, start2)
            right = min(end1, end2)

            if left <= right:
                res.append([left, right])

            # 谁先结束，谁往后走
            if end1 < end2:
                i += 1
            else:
                j += 1

        return res


# @lc code=end
sol = Solution()
res = sol.intervalIntersection(firstList=[[1, 3], [5, 9]], secondList=[])
print(res)
