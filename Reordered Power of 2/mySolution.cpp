bool reorderedPowerOf2(int N)
{
    std::string s = std::to_string(N);
    sort(s.begin(), s.end());
    std::vector<string> v;
    int n = N;
    for (size_t i = 0; i <= 31; ++i)
    {
        size_t twoPowers = pow(2, i);
        std::string st = std::to_string(twoPowers);
        sort(st.begin(), st.end());
        v.push_back(st);
    }
    auto p = find(v.begin(), v.end(), s);
    return p != v.end();
}
