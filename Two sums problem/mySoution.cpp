class Solution
{
public:
    vector<int> twoSum(vector<int> &nums, int target)
    {
        vector<int> ret;
        map<int, int> m;
        map<int, int>::iterator iter;

        for (int i = 0; i < nums.size(); i++)
        {
            iter = m.find(target - nums[i]);
            if (iter != m.end())
            {
                ret.push_back(i);
                ret.push_back(iter->second);
                break;
            }
            m.insert(pair<int, int>(nums[i], i));
        }
        return ret;
    }
};