/*
 * @lc app=leetcode.cn id=338 lang=cpp
 *
 * [338] 比特位计数
 */
#include <vector>
using namespace std;
// @lc code=start
class Solution
{
public:
    vector<int> countBits(int n)
    {
        vector<int> result(n + 1, 0);

        for (int i = 1; i <= n; ++i)
        // 这里从1开始，就是已经设置了初始条件，result[0]=0
        {
            result[i] = result[i >> 1] + (i & 1);
            // 右移一位，并确定一下最后一位是不是1
        }
        return result;
    }
};
// @lc code=end
