static std::vector<long long> decompose(long long n)
{
    std::vector<long long> d;
    long long goal = 0, cur;
    d.push_back(n);
    while (d.size() > 0)
    {
        cur = d.back();
        d.pop_back();
        goal += std::pow(cur, 2);
        for (long long i = cur - 1; i > 0; --i)
        {
            if ((goal - std::pow(i, 2)) >= 0)
            {
                goal -= pow(i, 2);
                d.push_back(i);
                if (goal == 0)
                {
                    std::reverse(d.begin(), d.end());
                    return d;
                }
            }
        }
    }
    d.clear();
    return d;
}