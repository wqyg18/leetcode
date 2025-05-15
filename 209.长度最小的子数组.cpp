/*
 * @lc app=leetcode.cn id=209 lang=cpp
 *
 * [209] 长度最小的子数组
 */
#include <vector>
using namespace std;
// @lc code=start
class Solution
{
public:
    int minSubArrayLen(int target, vector<int> &nums)
    {
        int n = nums.size();
        int start = 0;
        int window_sum = 0;
        int min_len = n + 1;

        for (int end = 0; end < n; ++end)
        {
            window_sum += nums[end];

            while (window_sum >= target)
            {
                min_len = min_len < end - start + 1 ? min_len : end - start + 1;
                window_sum -= nums[start];
                start++;
            }
        }
        return min_len == n + 1 ? 0 : min_len; // 注意不存在最小子数组的情况
    }
};
// @lc code=end
