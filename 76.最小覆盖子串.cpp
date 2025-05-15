/*
 * @lc app=leetcode.cn id=76 lang=cpp
 *
 * [76] 最小覆盖子串
 */
#include <string>
#include <unordered_map>
using namespace std;
// @lc code=start
class Solution
{
public:
    string minWindow(string s, string t)
    {
        unordered_map<char, int> need;
        for (char ch : t)
            need[ch]++;

        int left = 0;
        int right = 0;
        int start = 0;
        int min_len = INT_MAX; // 从0开始的子串长度
        int valid = 0; // 记录完成 字符数 匹配的 数量
        unordered_map<char, int> window;

        while (right < s.length())
        {
            char c = s[right];
            right++;
            if (need.count(c))
            {
                window[c]++;

                if (need[c] == window[c])
                {
                    valid++;
                }
            }

            while (valid == need.size()) // unordered_map.size() 返回key number
            {
                if (right - left < min_len)
                {
                    start = left;
                    min_len = right - left;
                }

                // 此时完成了所有字符的匹配，需要尝试缩减字符串，肯定是最左边往右挪一位
                char d = s[left];
                left++;

                if (need.count(d))
                {
                    if (need[d] == window[d])
                    {
                        valid--; // 因为往右挪之后肯定就不等了
                    }

                    window[d]--;
                }
            }
        }
        return min_len == INT_MAX ? "" : s.substr(start, min_len);
    }
};
// @lc code=end
