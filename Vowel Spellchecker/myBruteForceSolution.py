class Solution {
    public:
    template < typename T >
    std:: pair < bool, int > findInVector(const std: : vector < T >  & vecOfElements, const T  & element){
        std: : pair < bool, int > result;
        // Find given element in vector
        auto it = std: : find(vecOfElements.begin(), vecOfElements.end(), element);
        if (it != vecOfElements.end())
        {
            result.second = distance(vecOfElements.begin(), it);
            result.first = true;}
        else
        {
            result.first = false;
            result.second = -1;}
        return result;}
    vector < string > spellchecker(vector < string > & wordlist, vector < string > & queries) {
        vector < string > lowercase, vowelCase, output;
        // wordListCpy = wordlist;
        for(auto it: wordlist){
            std: : transform(it.begin(), it.end(), it.begin(), [](unsigned char c){return std: : tolower(c); });
            lowercase.push_back(it);}
        for(auto it: lowercase){
            for(size_t i=0; i < it.length(); ++i){
                if(it[i] == 'a' | | it[i] == 'e' | | it[i] == 'i' | | it[i] == 'o' | | it[i] == 'u'){
                    it[i] = '0';}
            }
            vowelCase.push_back(it);}
        for(auto it: queries){
            // auto itr = find(wordlist.begin(), wordlist.end(), it);
            std:: pair < bool, int > isFound = findInVector < string > (wordlist, it);
            if(isFound.first){output.push_back(wordlist[isFound.second]); continue; }
            std: : transform(it.begin(), it.end(), it.begin(), [](unsigned char c){return std: : tolower(c); });
            std:: pair < bool, int > isLowerCase = findInVector < string > (lowercase, it);
            if(isLowerCase.first){output.push_back(wordlist[isLowerCase.second]); continue; }
            for(size_t i=0; i < it.length(); ++i){
                if(it[i] == 'a' | | it[i] == 'e' | | it[i] == 'i' | | it[i] == 'o' | | it[i] == 'u'){
                    it[i] = '0';}
            }
            std:: pair < bool, int > isVowelCase = findInVector < string > (vowelCase, it);


            if(isVowelCase.first){output.push_back(wordlist[isVowelCase.second]); continue; }

            output.push_back("");}
        return output; }
};
