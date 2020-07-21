/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int rangeSumBST(TreeNode* root, int L, int R) {
        int* total = new int;
        *total = 0;
        helper(total, root, L, R);
        int val = *total;
        delete total;
        return val;   
    }
    
    void helper(int * tot, TreeNode* root, int L, int R){
        if (not root){
            return;
        }
        if (root->val >= L and root->val <= R) {
            *tot += root->val;
        }
        if (root->left){
            helper(tot, root->left, L, R);
        }
        if (root->right){
            helper(tot, root->right, L, R);
        }
    }
};
