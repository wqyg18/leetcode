#
# @lc app=leetcode.cn id=225 lang=python3
#
# [225] 用队列实现栈
#
from collections import deque


# @lc code=start
class MyStack:

    def __init__(self):
        self.queue = deque()
        self.help_queue = deque()

    def push(self, x: int) -> None:
        self.help_queue.append(x)
        while self.queue:
            self.help_queue.append(self.queue.popleft())
        self.queue = self.help_queue
        self.help_queue = deque()

    def pop(self) -> int:
        return self.queue.popleft()

    def top(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return not self.queue


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
# @lc code=end
