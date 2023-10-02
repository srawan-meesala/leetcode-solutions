struct ListNode {
    
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}

};

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

    bool isPalindrome(ListNode* head) {

        ListNode* t = head;
        ListNode* u = head;

        while(t->next && t->next->next){
            t = t->next->next;
            u = u->next;
        }

        ListNode* sec = reverseList(u->next);
        u->next = nullptr;
        ListNode* fir = head;

        while(fir && sec) {
            if(fir->val != sec->val){
                return false;
            }else{
                fir = fir->next;
                sec = sec->next;
            }
        }

        return true;

    }
};