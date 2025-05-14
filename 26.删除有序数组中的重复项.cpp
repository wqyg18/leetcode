/*
 * @lc app=leetcode.cn id=26 lang=cpp
 *
 * [26] 删除有序数组中的重复项
 */
#include <vector>
using namespace std;
// @lc code=start
class Solution
{
public:
    int removeDuplicates(vector<int> &nums)
    {
        int n = nums.size();
        if (n == 0)
            return 0;
        int slow = 0;
        for (int fast = 0; fast < n; ++fast)
        {
            if (nums[fast] != nums[slow])
            {
                nums[++slow] = nums[fast];
            }
        }
        return slow + 1;
    }
};
// @lc code=end
