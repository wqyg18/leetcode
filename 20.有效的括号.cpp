/*
 * @lc app=leetcode.cn id=20 lang=cpp
 *
 * [20] 有效的括号
 */
#include <string>
#include <stack>
using namespace std;
// @lc code=start
class Solution
{
public:
    bool isValid(string s)
    {
        if (s.size() % 2 != 0)
        {
            return false;
        }

        stack<char> st;
        for (int i = 0; i < s.size(); i++)
        {
            char ch = s[i];
            // 遇到左侧括号
            if (ch == '(')
            {
                st.push(')');
            }
            else if (ch == '[')
            {
                st.push(']');
            }
            else if (ch == '{')
            {
                st.push('}');
            }
            // 遇到右侧括号
            else if (st.empty() || st.top() != ch)
            {
                return false;
            }
            else
            {
                st.pop();
            }
        }
        return st.empty();
    }
};
// @lc code=end
