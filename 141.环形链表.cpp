/*
 * @lc app=leetcode.cn id=141 lang=cpp
 *
 * [141] 环形链表
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
#include <unordered_set>
using namespace std;
class Solution
{
public:
    bool hasCycle(ListNode *head)
    {
        unordered_set<ListNode *> seen;
        while (head != nullptr)
        {
            if (seen.count(head))
            {
                return true;
            }
            seen.insert(head);
            head = head->next;
        }
        return false;
    }
};
// @lc code=end
