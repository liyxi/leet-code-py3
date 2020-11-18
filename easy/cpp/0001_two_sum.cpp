#include <map>

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {

        int i = 0, j = 0;
        int nums_len = nums.size();
        std::map<int, int> value2index;
        vector<int> results;

        for (i = 0; i < nums_len; i++) {
            value2index[nums[i]] = i;
        }

        for (i = 0; i < nums_len; i++) {
            int cand = target - nums[i];
            if (value2index.count(cand) > 0) {
                j = value2index[cand];
                if (j != i) {
                    break;
                }
            }
        }
        results.push_back(i);
        results.push_back(j);
        return results;
    }
};
