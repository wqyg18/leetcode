/*
 * @lc app=leetcode.cn id=73 lang=cpp
 *
 * [73] 矩阵置零
 */

// @lc code=start
#include <unordered_set>
using namespace std;

// 直接使用第一行第一列当做之前的两个set
// 还需要额外两个flag记录第一行第一列是否含有0
class Solution
{
public:
    void setZeroes(vector<vector<int>> &matrix)
    {
        int m = matrix.size();
        int n = matrix[0].size();
        bool firstRowZero = false, firstColZero = false;

        // 判断首行首列是否需要置零
        for (int j = 0; j < n; ++j)
            if (matrix[0][j] == 0)
                firstRowZero = true;

        for (int i = 0; i < m; ++i)
            if (matrix[i][0] == 0)
                firstColZero = true;

        // 填充首行首列
        for (int i = 1; i < m; ++i)
        {
            for (int j = 1; j < n; ++j)
            {
                if (matrix[i][j] == 0)
                {
                    matrix[i][0] = 0;
                    matrix[0][j] = 0;
                }
            }
        }

        // 按照首行首列置零
        for (int i = 1; i < m; ++i)
        {
            for (int j = 1; j < n; ++j)
            {
                if (matrix[i][0] == 0 || matrix[0][j] == 0)
                {
                    matrix[i][j] = 0;
                }
            }
        }
        // 最后处理首行首列
        if (firstRowZero)
        {
            for (int j = 0; j < n; ++j)
                matrix[0][j] = 0;
        }
        if (firstColZero)
        {
            for (int i = 0; i < m; ++i)
                matrix[i][0] = 0;
        }
    }
};
// @lc code=end
