class Solution
{
public:
    vector<int> advantageCount(vector<int> &A, vector<int> &B)
    {
        vector<int> v = B;
        vector<int> ans;
        sort(v.begin(), v.end());
        sort(A.begin(), A.end());
        map<int, vector<int>> m;
        int i = 0;
        int j = B.size() - 1;
        while (i <= j)
        {
            if (A[i] > v[i])
            {
                auto itr = m.find(v[i]);

                if (itr != m.end())
                {
                    vector<int> tmp = m[v[i]];
                    tmp.push_back(A[i]);
                    itr->second = tmp;
                    tmp.clear();
                }
                else
                {
                    vector<int> tmp;
                    tmp.push_back(A[i]);
                    m.insert({v[i], tmp});
                    tmp.clear();
                }
                i += 1;
            }
            else
            {
                int temp = v[j];
                v.pop_back();
                v.insert(v.begin() + i, temp);
                auto itr = m.find(v[i]);
                if (itr != m.end())
                {
                    vector<int> tmp = m[v[i]];
                    tmp.push_back(A[i]);
                    itr->second = tmp;
                    tmp.clear();
                }
                else
                {
                    vector<int> tmp;
                    tmp.push_back(A[i]);
                    m.insert({v[i], tmp});
                    tmp.clear();
                }
                i += 1;
            }
        }
        for (int k = 0; k < B.size(); ++k)
        {
            auto it = m.find(B[k]);
            vector<int> temp = it->second;
            int t = temp.back();
            temp.pop_back();
            it->second = temp;
            ans.push_back(t);
        }
        return ans;
    }
};