struct ListNode {
    
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}

};

class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        if(head==nullptr){
            return head;
        }
        ListNode* first = new ListNode(-1);
        first->next = head;
        ListNode* t = first;
        ListNode* u = first;
        for(int i=0; i<n;i++){
            t = t->next;
        }
        while(t->next){
            t = t->next;
            u = u->next;
        }
        u->next = u->next->next;
        return first->next;
    }
};