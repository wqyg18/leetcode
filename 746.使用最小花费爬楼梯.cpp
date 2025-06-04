/*
 * @lc app=leetcode.cn id=746 lang=cpp
 *
 * [746] 使用最小花费爬楼梯
 */
#include <vector>
using namespace std;
// @lc code=start
class Solution
{
public:
    int minCostClimbingStairs(vector<int> &cost)
    {
        vector<int> dp(cost.size() + 1);
        // 因为状态转移方程只和i-1，i-2有关，所以可以直接使用两个变量
        int dp0 = 0;
        int dp1 = 0;
        int dpi;

        for (int i = 2; i <= cost.size(); i++)
        {
            dpi = min(dp1 + cost[i - 1], dp0 + cost[i - 2]);

            dp0 = dp1;
            dp1 = dpi;
        }
        return dpi;
    }
};
// @lc code=end
