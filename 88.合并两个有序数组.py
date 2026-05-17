#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#
from typing import List


# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # 从后往前遍历, 依次拿最大值
        # 如果是从前往后, 会覆盖掉原有的值, 不好处理
        i, j = m - 1, n - 1
        k = m + n - 1

        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1

            k -= 1

        # 补全剩下的j, 不需要管剩下的i, 因为i已经是正确的位置了
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1


# @lc code=end
