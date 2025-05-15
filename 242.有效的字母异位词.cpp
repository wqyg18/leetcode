/*
 * @lc app=leetcode.cn id=242 lang=cpp
 *
 * [242] 有效的字母异位词
 */
#include <string>
#include <unordered_map>
using namespace std;
// @lc code=start
class Solution
{
public:
    bool isAnagram(string s, string t)
    {
        if (s.length() != t.length())
        {
            return false;
        }

        unordered_map<char, int> count;
        for (char ch : s)
            count[ch]++;
        for (char ch : t)
        {
            if (--count[ch] < 0)
            {
                return false;
            }
        }
        return true;
    }
};
// @lc code=end
