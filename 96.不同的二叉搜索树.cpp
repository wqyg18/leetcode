/*
 * @lc app=leetcode.cn id=96 lang=cpp
 *
 * [96] 不同的二叉搜索树
 */
#include <vector>
using namespace std;
// @lc code=start
class Solution
{
public:
    int numTrees(int n)
    {
        vector<int> dp(n + 1, 0);
        dp[0] = 1;
        // 相当于0个节点也是一种

        for (int i = 1; i <= n; i++)
        {
            for (int j = 1; j <= i; j++)
            {
                dp[i] += dp[j - 1] * dp[i - j];
                // 左边j-1，右边i-j
                // 相乘是因为不同的组合就是不同的树
            }
        }
        return dp[n];
    }
};
// @lc code=end
