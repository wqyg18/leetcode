/*
 * @lc app=leetcode.cn id=392 lang=cpp
 *
 * [392] 判断子序列
 */
#include <string>
using namespace std;
// @lc code=start
class Solution
{
public:
    bool isSubsequence(string s, string t)
    {
        int n = s.size(), m = t.size();
        if (n == 0)
            return true;
        int i = 0, j = 0;

        while (i < n && j < m)
        {
            if (s[i] == t[j])
            {
                i++;
            }

            if (i == n)
            {
                return true;
            }

            j++;
        }
        return false;
    }
};
// @lc code=end
