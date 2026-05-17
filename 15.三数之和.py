#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#


# @lc code=start
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # 排序后, 针对每一个i, 求two sum
        # 重要的是去重, 由于本身保证了i,left,right三个指针不同, 即满足题目要求的三个下标不同
        # 只需要保证，对于i,left,right三个指针对应的数字，分别没有和自己重复就可以了
        nums.sort()
        res = []

        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1

            # 首先对i去重, 从第二个开始
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                if current_sum < 0:
                    left += 1
                elif current_sum > 0:
                    right -= 1
                elif current_sum == 0:
                    # 找到了一个答案
                    res.append([nums[i], nums[left], nums[right]])

                    # 前面对i去重了, 还需要对left和right分别去重
                    while left < right and nums[left + 1] == nums[left]:
                        left += 1
                    while left < right and nums[right - 1] == nums[right]:
                        right -= 1

                    # 还可能存在另外的答案
                    left += 1
                    right -= 1

        return res


# @lc code=end
sol = Solution()
res = sol.threeSum([-1, 0, 1, 2, -1, -4])
print(res)
