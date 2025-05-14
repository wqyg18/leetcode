/*
 * @lc app=leetcode.cn id=283 lang=cpp
 *
 * [283] 移动零
 */
#include <vector>
#include <iostream>
using namespace std;
// @lc code=start
class Solution {
    public:
        void moveZeroes(vector<int>& nums) {
            int n = nums.size();
            int nonZeroIndex = 0;
    
            for (int current = 0; current < n; ++current) {
                if (nums[current] != 0) {
                    nums[nonZeroIndex++] = nums[current];
                }
            }
    
            // 填充剩余位置为 0
            for (int i = nonZeroIndex; i < n; ++i) {
                nums[i] = 0;
            }
        }
    };
// @lc code=end
