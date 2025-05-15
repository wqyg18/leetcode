/*
 * @lc app=leetcode.cn id=844 lang=cpp
 *
 * [844] 比较含退格的字符串
 */
#include <string>
using namespace std;
// @lc code=start
class Solution
{
public:
    bool backspaceCompare(string s, string t)
    {
        int s_pos = s.length() - 1;
        int t_pos = t.length() - 1;

        int s_skip = 0;
        int t_skip = 0;

        while (s_pos >= 0 || t_pos >= 0)
        {
            while (s_pos >= 0)
            {
                if (s[s_pos] == '#')
                {
                    s_skip++;
                    s_pos--;
                }
                else if (s_skip > 0)
                {
                    s_skip--;
                    s_pos--;
                }
                else
                {
                    break;
                }
            }

            while (t_pos >= 0)
            {
                if (t[t_pos] == '#')
                {
                    t_skip++;
                    t_pos--;
                }
                else if (t_skip > 0)
                {
                    t_skip--;
                    t_pos--;
                }
                else
                {
                    break;
                }
            }

            if (s_pos >= 0 && t_pos >= 0 && s[s_pos] != t[t_pos])
                return false;
            if ((s_pos >= 0) != (t_pos >= 0))
                return false;

            s_pos--;
            t_pos--;
        }
        return true;
    }
};
// @lc code=end
