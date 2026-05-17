#
# @lc app=leetcode.cn id=832 lang=python3
#
# [832] 翻转图像
#
from typing import List


# @lc code=start
class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for row in image:
            left, right = 0, len(row) - 1
            while left <= right:
                # 交换并反转：两个位置的值互换后再各自取反
                row[left], row[right] = 1 - row[right], 1 - row[left]
                left += 1
                right -= 1
        return image


# @lc code=end
sol = Solution()
res = sol.flipAndInvertImage(image=[[1, 1, 0], [1, 0, 1], [0, 0, 0]])
print(res)
