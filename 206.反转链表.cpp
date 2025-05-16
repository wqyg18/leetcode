/*
 * @lc app=leetcode.cn id=206 lang=cpp
 *
 * [206] 反转链表
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution
{
public:
    ListNode *reverseList(ListNode *head)
    {
        return recur(head,nullptr);
    }

private:
    ListNode *recur(ListNode *cur, ListNode *pre)
    {
        // 终止条件
        if (cur == nullptr)
            return pre;

        ListNode *res = recur(cur->next, cur);
        cur->next = pre;
        return res;
    }
};
// @lc code=end
