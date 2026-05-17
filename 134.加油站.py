#
# @lc app=leetcode.cn id=134 lang=python3
#
# [134] 加油站
#
from typing import List


# @lc code=start
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total = 0
        tank = 0
        start = 0

        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            # 这里不需要去取余进行计算, 其实可以直接一直统计所有的diff, 如果start在最后, 那么前面的diff已经加过了
            # 题目保证了, 答案唯一, 因此只需要往后一直遍历, 找到第一个一直到结尾tank都是正的就可以了
            total += diff
            tank += diff

            # 这里贪心, 贪的是, 如果tank<0了, 那么说明, 之前的所有都不能采用
            # 因为 能一直往前走, 肯定是tank >=0, 那么从中间结点, 比如说从油箱为0开始走
            # 那么结果一定不会更好, 最多持平, 所以直接跳过这些点
            if tank < 0:
                start = i + 1
                tank = 0

        if total < 0:
            return -1
        return start


# @lc code=end
sol = Solution()
res = sol.canCompleteCircuit([5, 8, 2, 8], [6, 5, 6, 6])
print(res)
