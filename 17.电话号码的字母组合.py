#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#
from typing import List


# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        result = [""]
        for i in range(len(digits)):
            result_tmp = []
            for prefix in result:
                for subfix in map[digits[i]]:
                    result_tmp.append(prefix + subfix)

            result = result_tmp

        return result


# @lc code=end
