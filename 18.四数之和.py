#
# @lc app=leetcode.cn id=18 lang=python3
#
# [18] 四数之和
#
from typing import List


# @lc code=start
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums)):
            # 去重第一个
            # 如果新一轮的这个值和之前的一样, 那么得到的结果肯定是已经有了的, 肯定重复
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, len(nums)):
                # 去重第二个
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                left = j + 1
                right = len(nums) - 1

                while left < right:
                    s = nums[i] + nums[j] + nums[left] + nums[right]

                    if s < target:
                        left += 1
                    elif s > target:
                        right -= 1
                    elif s == target:
                        res.append([nums[i], nums[j], nums[left], nums[right]])

                        # 对第三个去重
                        while left < right and nums[left + 1] == nums[left]:
                            left += 1
                        # 对第四个去重
                        while left < right and nums[right - 1] == nums[right]:
                            right -= 1

                        # 看看有没有其他答案(同一个i,j情况下)
                        left += 1
                        right -= 1

        return res


# @lc code=end
res = Solution().fourSum([2, 2, 2, 2, 2], 8)
print(res)
