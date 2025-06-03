/*
 * @lc app=leetcode.cn id=376 lang=cpp
 *
 * [376] 摆动序列
 */
#include <vector>
using namespace std;
// @lc code=start
class Solution
{
public:
    int wiggleMaxLength(vector<int> &nums)
    {
        if (nums.size() < 2)
            return nums.size();

        int up = 1, down = 1;
        // up,down表示当前元素作为up，down时的最长摆动序列

        for (int i = 1; i < nums.size(); i++)
        {
            if (nums[i] > nums[i - 1])
                up = down + 1;
            else if (nums[i] < nums[i - 1])
                down = up + 1;
            // 连续的上升或者下降是不会影响结果的，因为down或者up没变
        }
        return max(up, down);
    }
};
// @lc code=end
