/*
 * @lc app=leetcode id=1 lang=cpp
 *
 * [1] Two Sum
 */

#include <vector>
#include <unordered_map>
using namespace std;

// @lc code=start
class Solution
{
public:
    vector<int> twoSum(vector<int> &nums, int target)
    {
        unordered_map<int, int> numMap; // <value,idx>
        for (int i = 0; i < nums.size(); ++i)
        {
            int complement = target - nums[i];

            if (numMap.count(complement))
            {
                return {numMap[complement], i};
            }

            numMap[nums[i]] = i;
        }

        return {};
    }
};
// @lc code=end
