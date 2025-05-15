/*
 * @lc app=leetcode.cn id=3 lang=cpp
 *
 * [3] 无重复字符的最长子串
 */
#include <string>
#include <unordered_set>
using namespace std;
// @lc code=start
class Solution
{
public:
    int lengthOfLongestSubstring(string s)
    {
        unordered_set<char> window;
        int left = 0;
        int max_len = 0;

        for (int right = 0; right < s.size(); ++right)
        {
            while (window.count(s[right]))
            {
                window.erase(s[left]);
                ++left;
            }
            window.insert(s[right]);
            max_len = max(max_len, right - left + 1);
        }
        return max_len;
    }
};
// @lc code=end
