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
    vector<int> rightSideView(TreeNode* root) {
        if (!root){
            return {};
        }
        int curLevel = 0;
        vector<int> *ans = new vector<int>;
        helper(curLevel, ans, root);
        
        return *ans;   
    }
    
    void helper(int curLevel, vector<int>* ans, TreeNode* root){
        curLevel += 1;
        if (curLevel > ans->size()){
            (*ans).push_back(root->val);
        }
        if (root->right){
            helper(curLevel, ans, root->right);
        }
        if (root->left){
            helper(curLevel, ans, root->left);
        }
    }

};
