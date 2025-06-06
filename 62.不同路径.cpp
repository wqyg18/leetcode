/*
 * @lc app=leetcode.cn id=62 lang=cpp
 *
 * [62] 不同路径
 */
#include <vector>
using namespace std;
// @lc code=start
class Solution
{
public:
    int uniquePaths(int m, int n)
    {
        // 利用滚动数组优化，只用一维列表实现
        vector<int> dp(n, 1);

        for (int i = 1; i < m; ++i)
        {
            for (int j = 1; j < n; ++j)
            {
                dp[j] = dp[j] + dp[j - 1];
                // i行j列 = i-1行j列 + i行j-1列
            }
        }
        return dp[n - 1];
    }
};
// @lc code=end
