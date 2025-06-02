/*
 * @lc app=leetcode.cn id=70 lang=cpp
 *
 * [70] 爬楼梯
 */

// @lc code=start
class Solution
{
public:
    int climbStairs(int n)
    {
        if (n <= 2)
        {
            return n;
        }

        int a = 1, b = 1, sum;
        for (int i = 2; i <= n; i++)
        {
            sum = a + b;
            b = a;
            a = sum;
        }
        return sum;
    }
};
// @lc code=end
