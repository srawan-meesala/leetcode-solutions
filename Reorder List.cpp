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
class Solution {
public:

    ListNode* reverseList(ListNode* head) {

        ListNode* curr = head;
        ListNode* prev = nullptr;

        while(curr){
            ListNode* nex = curr->next;
            curr->next = prev;
            prev=curr;
            curr=nex;
        }

        return prev;

    }

    void reorderList(ListNode* head) {
        ListNode* t = head;
        ListNode* u = head;

        if(head==NULL || head->next==NULL){
            return;
        }

        while(t->next && t->next->next){
            t = t->next->next;
            u = u->next;
        }

        ListNode* sec = reverseList(u->next);
        u->next = nullptr;
        ListNode* fir = head;
        ListNode* k;
        ListNode* p;
        while(fir && sec && fir->next && sec->next){
            k = fir->next;
            p = sec->next;
            fir->next = sec;
            sec->next = k;
            fir = k;
            sec = p;
        }
        if(sec->next == nullptr){
            if(fir->next){
                k = fir->next;
            }else{
                k = NULL;
            }
            fir->next = sec;
            sec->next = k;
        }
    }
};