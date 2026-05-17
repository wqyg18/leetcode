#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并 K 个升序链表
#
from typing import List, Optional
import heapq


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
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:        
        dummy = ListNode(0, None)
        current = dummy

        # len(lists)容量的最小堆, 每次pop堆顶, 就是当前的最小元素,依次连接
        min_heaq = []
        # heap中没办法直接存ListNode,没办法比较,但是可以存元组
        # 直接存(node.val, node)可能出现相同的val, 可以存(node.val, id(node), node)

        # 将每个链表的头放到heaq中
        for node in lists:
            if node:
                heapq.heappush(min_heaq, (node.val, id(node), node))

        # 只要heaq还有元素, 那么就继续pop
        while min_heaq:
            _, _, node = heapq.heappop(min_heaq)
            current.next = node
            current = node

            if node.next:
                heapq.heappush(min_heaq, (node.next.val, id(node.next), node.next))

        return dummy.next


# @lc code=end
