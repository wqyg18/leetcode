#
# @lc app=leetcode.cn id=738 lang=python3
#
# [738] 单调递增的数字
#


# @lc code=start
class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        # 要找最大数字, 从前往后看
        # 首先看第一个数字是不是小于第二个数字， 如果不是，对第一个数字减去1， 然后后面直接取9
        # 如果第一个数字小于等于第二个数字， 如果不是， 对第二个数字减去1， 然后后面取9

        # 从前往后，找到首个出现的， 前一个数字小于后一个数字的位置\

        # 更优雅的思路是从后往前
        nums = list(str(n))
        nums = list(map(int, nums))

        # marker 表示从哪个位置开始，后面全部改成 9
        marker = len(nums)

        for i in range(len(nums) - 1, 0, -1):
            if nums[i] < nums[i - 1]:
                marker = i
                nums[i - 1] -= 1

            nums[marker:] = [9] * (len(nums) - marker)

        return int("".join(map(str, nums)))


# @lc code=end
sol = Solution()
res = sol.monotoneIncreasingDigits(120)
print(res)
