/*
 * @lc app=leetcode.cn id=1049 lang=cpp
 *
 * [1049] 最后一块石头的重量 II
 */
#include <vector>
#include <numeric>
using namespace std;
// @lc code=start
class Solution
{
public:
    int lastStoneWeightII(vector<int> &stones)
    {
        vector<int> dp(15001, 0);
        int sum = accumulate(stones.begin(), stones.end(), 0);

        // 尽可能拼成sum / 2大小的背包，剩下的也是接近sum / 2的
        int target = sum / 2;
        for (int i = 0; i < stones.size(); i++)
        {
            for (int j = target; j >= stones[i]; j--)
            {
                // 01背包迭代公式dp[j] = max(dp[j], dp[j-weights[i]] + values[i])
                dp[j] = max(dp[j], dp[j - stones[i]] + stones[i]);
            }
        }

        // dp[target]就是target容量下最多能装的重量了
        int res = sum - dp[target] - dp[target];
        return res;
    }
};
// @lc code=end
