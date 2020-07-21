class Solution {
public:
    bool isAnagram(string s, string t) {
        int sLen = s.length();
        int tLen = t.length();
        if (sLen != tLen){
            return false;
        }
        vector<int> freqs(26, 0);
        vector<int> freqt(26, 0);
        int idxs = 0;
        int idxt = 0;
        for (int i = 0; i < sLen; i++){
            idxs = s[i] - int('a');
            idxt = t[i] - int('a');
            freqs[idxs] += 1;
            freqt[idxt] += 1;
        }
                
        for (int i = 0; i < 26; i++){
            if (freqs[i] != freqt[i]){
                return false;
            }
        }
        return true;
    }
};
