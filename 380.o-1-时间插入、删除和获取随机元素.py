#
# @lc app=leetcode.cn id=380 lang=python3
#
# [380] O(1) 时间插入、删除和获取随机元素
#

"""
| 能力   | dict | list |
| ---- | ---- | ---- |
| 查找   | O(1) | O(n) |
| 删除   | O(1) | O(n) |
| 随机访问 | ❌    | O(1) |
"""

import random
# @lc code=start
class RandomizedSet:

    def __init__(self):
        self.nums = []  # 存值
        self.val_to_index = {}  # val -> index

    def insert(self, val: int) -> bool:
        if val in self.val_to_index:
            return False
        self.nums.append(val)
        self.val_to_index[val] = len(self.nums) - 1

        return True

    def remove(self, val: int) -> bool:
        if val not in self.val_to_index:
            return False
        
        # 使用list的pop方法实现O(1)
        # 将val与list[-1]对调
        idx = self.val_to_index[val]
        last_value = self.nums[-1]

        self.nums[idx] = last_value
        self.val_to_index[last_value] = idx
        
        self.nums[-1] = val

        self.nums.pop()
        self.val_to_index.pop(val)

        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# @lc code=end
