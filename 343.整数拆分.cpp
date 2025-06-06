/*
 * @lc app=leetcode.cn id=343 lang=cpp
 *
 * [343] 整数拆分
 */
#include <vector>
#include <algorithm>
using namespace std;
// @lc code=start
class Solution
{
public:
    int integerBreak(int n)
    {
        // 注意是求n对应的拆分，dp[i]表示正整数i拆分可以得到的最大乘积
        // 这样用n+1而不是n，比较方便处理
        vector<int> dp(n + 1);

        // 初始化
        dp[2] = 1;

        // 遍历j
        // dp[i] 有两种情况，一种是拆分两个数字，j*(i-j)
        //                  一种是拆分多个，也就是有j的情况下，剩下的（i-j）拆分，即为dp[i-j]
        for (int i = 3; i <= n; i++)
        {
            for (int j = 1; j <= i / 2; j++)
            {
                // 如果之前的dp[i]是最大，当然要保留，因为这里是在遍历j
                dp[i] = max(dp[i], max(j * (i - j), j * dp[i - j]));
            }
        }
        return dp[n];
    }
};
// @lc code=end
