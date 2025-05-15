/*
 * @lc app=leetcode.cn id=904 lang=cpp
 *
 * [904] 水果成篮
 */
#include <vector>
#include <unordered_map>
using namespace std;
// @lc code=start
class Solution
{
public:
    int totalFruit(vector<int> &fruits)
    {
        unordered_map<int, int> basket;
        int left = 0;
        int max_len = 0;

        for (int right = 0; right < fruits.size(); ++right)
        {
            basket[fruits[right]]++; // 直接记录所有水果种类并计数

            while (basket.size() > 2)
            {
                basket[fruits[left]]--;
                if (basket[fruits[left]] == 0)
                {
                    basket.erase(fruits[left]);
                }
                left++;
            }
            max_len = max(max_len, right - left + 1);
        }
        return max_len;
    }
};
// @lc code=end