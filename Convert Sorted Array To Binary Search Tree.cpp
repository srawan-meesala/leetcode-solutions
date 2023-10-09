struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:

    TreeNode* BST(vector<int>& nums, int left, int right) {
        if(left>right){
            return nullptr;
        }
        int p = (left+right)/2;
        TreeNode* ans = new TreeNode(nums[p]);
        ans->left = BST(nums, left, p-1);
        ans->right = BST(nums, p+1, right);
        return ans;
    }

    TreeNode* sortedArrayToBST(vector<int>& nums) {
        int n = nums.size();
        int k = n/2;
        TreeNode* ans = new TreeNode(nums[k]);
        ans->left = BST(nums, 0, k-1);
        ans->right = BST(nums, k+1, n-1);
        return ans;
    }
};