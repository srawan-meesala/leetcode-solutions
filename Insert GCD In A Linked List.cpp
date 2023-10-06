struct ListNode {
    
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}

};

class Solution {
public:
    ListNode* insertGreatestCommonDivisors(ListNode* head) {
        ListNode* t = head;
        while(t->next){
            ListNode* p = t->next;
            ListNode* k = new ListNode(gcd(t->val, t->next->val));
            t->next = k;
            k->next = p;
            t = p;
        }
        return head;
    }
};