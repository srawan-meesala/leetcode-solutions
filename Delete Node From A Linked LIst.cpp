struct ListNode {
    
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}

};

class Solution {
public:
    void deleteNode(ListNode* node) {
        ListNode* t = node;
        while(t->next->next!=nullptr && t->next!=nullptr){
            t->val = t->next->val;
            t = t->next;
        }
        t->val = t->next->val;
        t->next = nullptr;
    }
};