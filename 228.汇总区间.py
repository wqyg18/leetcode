#
# @lc app=leetcode.cn id=228 lang=python3
#
# [228] 汇总区间
#
from typing import List


# @lc code=start
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:

        if not nums:
            return []
        start = nums[0]
        offset = nums[0] - 0
        res = []
        for i in range(len(nums)):

            # 满足条件, 一直往后遍历
            if offset + i == nums[i]:
                end = nums[i]
                continue

            # 不满足条件, 保存当前区间, 然后进行下一个区间的遍历
            if start == end:
                res.append(str(start))
            else:
                res.append(str(start) + "->" + str(end))

            start = nums[i]
            offset = nums[i] - i
            end = nums[i]

        # 保存最后一个区间
        if start == end:
            res.append(str(start))
        else:
            res.append(str(start) + "->" + str(end))

        return res


# @lc code=end
sol = Solution()
res = sol.summaryRanges([0, 2, 3, 4, 6, 8, 9])
print(res)
