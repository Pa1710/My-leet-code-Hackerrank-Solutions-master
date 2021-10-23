public class MySolution {
    public boolean isAlienSorted(String[] words, String order) {
        Map<Character, Integer> h = new HashMap<Character, Integer>();
        for(int i = 0; i < 26; ++i){
            h.put(order.charAt(i),i);
        }
        for(int i = 0; i < words.length - 1; ++i){
            int j = i + 1;
            String s1 = words[i];
            String s2 = words[j];
            //System.out.println(s1 + " " + s2);
            for(int k = 0; k < s2.length(); ++k){
                if(k == s1.length()){break;}
                int lex1 = h.get(s1.charAt(k));
                int lex2 = h.get(s2.charAt(k));
                //System.out.println(lex1 + " " + lex2);
                if(k == s2.length() - 1){
                    if(lex1 < lex2){break;}
                    if(lex1 > lex2){return false;}
                    if(lex1 == lex2){
                        if(s1.length() == s2.length()){break;}
                        if(s1.length() > s2.length()){return false;}
                    }
                }
                if(lex1 < lex2){break;}
                if(lex1 > lex2){return false;}
                if(lex1 == lex2){continue;}
            }
        }
        return true;
    }
}
