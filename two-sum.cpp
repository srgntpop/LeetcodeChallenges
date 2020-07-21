
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> retVect;
        map<int, int> mymap;
        int complement;
        int idx = 0;
        for (auto itr : nums){
            complement = target - itr;
            if (mymap.count(complement) > 0){
                return {idx, mymap[complement]};
            }
            cout << itr << " " << idx << " " << endl;
            mymap[itr] = idx;
            idx++;
        }
        return retVect;
    }
};
