#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        left = list1
        right = list2
        dummy = ListNode()
        current = dummy

        while left and right:
            if left.val < right.val:
                current.next = left
                left = left.next
                current = current.next
            elif left.val >= right.val:
                current.next = right
                right = right.next
                current = current.next

        if left:
            current.next = left
        if right:
            current.next = right

        return dummy.next


# @lc code=end
