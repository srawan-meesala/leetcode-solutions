struct ListNode {
    
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}

};

class Solution {
public:

    ListNode* merge(ListNode* l1, ListNode* l2) {
        if(l1==nullptr){return l2;}
        if(l2==nullptr){return l1;}
        if(l1->val<l2->val){
            l1->next = merge(l1->next, l2);
            return l1;
        }else{
            l2->next = merge(l1, l2->next);
            return l2;
        }
    }

    ListNode* sortList(ListNode* head) {
        if (head==nullptr || head->next==nullptr){return head;}
        ListNode* slow = head;
        ListNode* fast = head;
        while(fast->next!=nullptr && fast->next->next!=nullptr) {
            slow = slow->next;
            fast = fast->next->next;
        }
        ListNode* u = slow->next;
        slow->next = nullptr;
        ListNode* l1 = sortList(head);
        ListNode* l2 = sortList(u);
        return merge(l1,l2);
    }
};