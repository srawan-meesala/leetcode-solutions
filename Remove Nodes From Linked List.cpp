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

    ListNode* removeNodes(ListNode* head) {
        if(head==nullptr || head->next==nullptr){
            return head;
        }
        ListNode* temp = reverseList(head);
        ListNode* t = temp;
        ListNode* u = t->next;
        while(u && u->next){
            if(u->val<t->val){
                t->next = u->next;
                u = t->next;
            }else{
                t = u;
                u = u->next;
            }
        }
        if(t->val>u->val){
            t->next = nullptr;
        }

        return reverseList(temp);
    }
};