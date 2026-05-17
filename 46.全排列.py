#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#
from typing import List
# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        path = []
        res = []
        def backtrack():
            if len(path) == len(nums):
                res.append(path[:])
                return

            for num in nums:
                if num in path:
                    continue
                
                # 全排列, 先拿第一个
                # 然后按照这个往后一直递归
                # 这一个的所有情况试完了，开始把这个换成另外一个开始试
                path.append(num)
                backtrack()
                path.pop()
        
        backtrack()
        return res
            


        
# @lc code=end
sol = Solution()
res = sol.permute(nums = [1,2,3])
print(res)
