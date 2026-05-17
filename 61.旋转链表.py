#
# @lc app=leetcode.cn id=61 lang=python3
#
# [61] 旋转链表
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
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # 轮转数组, 数组的思路是, 1整体reverse, 2: 前k reverse, 3: 剩余部分reverse

        # 但是这里是链表, 需要使用双指针去实现

        if not head or not head.next:
            return head

        # 首先求长度n
        n = 0
        node = head
        while node:
            node = node.next
            n += 1

        # k % n
        k = k % n
        if k == 0:
            return head

        slow = head
        fast = head
        # 往右k个, 那么 倒数第k个(1-based)是新尾结点, 倒数第(k+1)和是新头结点
        # 为了找到倒数第k个点, 可以这样做, slow,fast都在head, fast先走k步, 然后slow和fast一起走
        # 知道fast为空, 此时fast在最后一个节点, 那么slow就是倒数第k个点

        for _ in range(k):
            fast = fast.next

        while fast.next:
            fast = fast.next
            slow = slow.next

        # 此时 fast在原来的尾结点
        # slow在新的尾结点
        # slow.next是新的头结点

        new_head = slow.next
        slow.next = None
        fast.next = head

        return new_head


# @lc code=end
