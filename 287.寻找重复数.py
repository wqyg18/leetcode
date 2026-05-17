#
# @lc app=leetcode.cn id=287 lang=python3
#
# [287] 寻找重复数
#
from typing import List


# @lc code=start
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # 模拟链表, slow,fast等是当前节点的地址
        # nums[slow],nums[fast]是next节点的地址
        
        # 所以前进一步就是 slow = nums[slow]
        # 两步就是 fast = nums[nums[fast]]
        
        # stage 1 找相遇点
        slow = nums[0]
        fast = nums[nums[0]]

        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        print(slow)
        # Stage 2: 寻找环的入口（也就是重复的数）
        # 此时 slow 和 fast 已经相等（都在相遇点）
        ptr1 = 0        # 回到起点
        ptr2 = slow     # 留在相遇点

        while ptr1 != ptr2: # 两个指针同步向后挪
            ptr1 = nums[ptr1]
            ptr2 = nums[ptr2]

        # 当它们相等时，这个位置就是环的入口，也就是那个重复的数字
        return ptr1


# @lc code=end
