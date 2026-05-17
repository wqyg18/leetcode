#
# @lc app=leetcode.cn id=622 lang=python3
#
# [622] 设计循环队列
#


# @lc code=start
class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [None] * k
        self.capacity = k
        self.head = 0  # 当前head元素的位置
        self.size = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.queue[(self.head + self.size) % self.capacity] = value
        self.size += 1
        return True

    # FIFO (First-In-First-Out, 先进先出)
    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.head]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[(self.head + self.size - 1) % self.capacity]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
# @lc code=end
