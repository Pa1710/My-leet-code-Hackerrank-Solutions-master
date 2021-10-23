class Solution {
    public:
    vector < string > spellchecker(vector < string > & wordlist, vector < string > & queries) {
        unordered_set < string > s(wordlist.begin(), wordlist.end());
        unordered_map < string, string > m, mm;
        vector < string > w(wordlist);
        for(int i=wordlist.size()-1; i >= 0; i--){
            for(auto & it: w[i]) it = tolower(it);
            m[w[i]] = wordlist[i];
            for(auto & it: w[i]) if(it == 'a' | | it == 'e' | | it == 'i' | | it == 'o' | | it == 'u') it = '0';
            mm[w[i]] = wordlist[i]; }
        for(auto & itr: queries){
            if(s.count(itr)) continue;
            for(auto & c: itr) c = tolower(c);
            if(m.count(itr)){
                itr = m[itr];
                continue;}
            for(auto & c: itr) if(c == 'a' | | c == 'e' | | c == 'i' | | c == 'o' | | c == 'u') c = '0';
            if(mm.count(itr)){
                itr = mm[itr];
                continue;}
            itr = ""; }
        return queries;}
};
