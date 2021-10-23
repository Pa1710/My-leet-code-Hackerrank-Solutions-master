class Solution
{
public:
    int lengthOfLongestSubstring(string s)
    {
        std::vector<string> v;
        size_t count = 0;
        size_t tcount = 0;
        for (size_t i = 0; i < s.length(); ++i)
        {
            char a = s[i];
            std::string s1;
            if (isblank(a))
            {
                s1 = " ";
            }

            s1.append(1, a);

            auto it = std::find(v.begin(), v.end(), s1);
            if (it != v.end())
            {
                if (tcount > count)
                {
                    count = tcount;
                }
                char itr = it - v.begin();
                v.erase(v.begin(), v.begin() + itr + 1);
                tcount = v.size();
            }
            v.push_back(s1);
            tcount += 1;
        }

        if (tcount > count)
        {
            count = tcount;
        }
        return count;
    }
};