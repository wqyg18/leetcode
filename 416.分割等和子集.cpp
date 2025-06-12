/*
 * @lc app=leetcode.cn id=416 lang=cpp
 *
 * [416] 分割等和子集
 */
#include <vector>
#include <numeric>
using namespace std;
// @lc code=start
class Solution
{
public:
    bool canPartition(vector<int> &nums)
    {
        // 01背包，weight和value均是nums
        vector<int> dp(10001, 0);
        int sum = accumulate(nums.begin(), nums.end(), 0);

        // 如果总和是奇数，显然不能分割成两个子集
        if (sum % 2 == 1)
            return false;
        // 即背包总容量是sum / 2，如果能够实现正好装满这个背包，则true
        int target = sum / 2;

        // 01背包
        for (int i = 0; i < nums.size(); i++)
        {
            for (int j = target; j >= nums[i]; j--)
            {
                // 01背包对应的是dp[j] = max(dp[j], dp[j - weight[i]] + value[i]);
                // 这里weight和value均是nums
                dp[j] = max(dp[j], dp[j - nums[i]] + nums[i]);
            }
        }

        if (dp[target] == target)
            return true;
        return false;
    }
};
// @lc code=end
