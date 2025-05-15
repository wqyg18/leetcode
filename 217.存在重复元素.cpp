/*
 * @lc app=leetcode.cn id=217 lang=cpp
 *
 * [217] 存在重复元素
 */
#include <unordered_set>
using namespace std;
// @lc code=start
class Solution
{
public:
    bool containsDuplicate(vector<int> &nums)
    {
        unordered_set<int> seen;
        for (int num : nums)
        {
            if (seen.count(num))
            {
                return true;
            }
            seen.insert(num);
        }
        return false;
    }
};
// @lc code=end
