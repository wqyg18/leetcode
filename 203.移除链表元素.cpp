/*
 * @lc app=leetcode.cn id=203 lang=cpp
 *
 * [203] 移除链表元素
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

#include <iostream>
using namespace std;

// struct ListNode
// {
//     int val;
//     ListNode *next;
//     ListNode(int x) : val(x), next(nullptr) {}
// };

class Solution
{
public:
    ListNode *removeElements(ListNode *head, int val)
    {
        // 处理头结点
        ListNode* dummy = new ListNode(0);
        dummy->next = head;

        ListNode *current = dummy;

        while (current->next != nullptr)
        {
            if (current->next->val == val)
            {
                ListNode *toDelete = current->next;
                current->next = current->next->next;

                delete toDelete;
            }
            else
            {
                current = current->next;
            }
        }
        return dummy->next;
    }
};
// @lc code=end
