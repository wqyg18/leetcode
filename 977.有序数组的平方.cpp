/*
 * @lc app=leetcode.cn id=977 lang=cpp
 *
 * [977] 有序数组的平方
 */
#include <vector>
using namespace std;

// @lc code=start
class Solution
{
public:
    vector<int> sortedSquares(vector<int> &nums)
    {
        int n = nums.size();
        int left = 0;
        int right = n - 1;
        vector<int> result(n);

        int pos = n - 1;

        while (left <= right)
        {
            if (abs(nums[left]) > abs(nums[right]))
            {
                result[pos] = nums[left] * nums[left];
                left++;
            }
            else
            {
                result[pos] = nums[right] * nums[right];
                right--;
            }
            pos--;
        }

        return result;
    }
};
// @lc code=end
