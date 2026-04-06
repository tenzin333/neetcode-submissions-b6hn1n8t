class Solution {
public:
    string minWindow(string s, string t) {
     
            int l=0;
            int r=0;
            unordered_map<char,int> smap;
            unordered_map<char,int> tmap;

            for(char c:t)
                tmap[c]++;
            int have =0,need=tmap.size();
            int size=INT_MAX;
            vector<int> res = {-1,-1};
        
            while(r<s.length()){
               
                smap[s[r]]++;
                if(tmap.find(s[r])!=tmap.end() && tmap[s[r]]==smap[s[r]]){
                   
                        have++;
                
                }
             

                 while(have==need){
                        if((r-l+1) < size){
                            res = {l,r};
                            size = r-l+1;
                        }
                        smap[s[l]]--;
                        if(tmap.find(s[l])!=tmap.end() && smap[s[l]] < tmap[s[l]]){
                                have--;   
                        }
                        l++;
                    }
                r++;
            }

            return size == INT_MAX ? "" : s.substr(res[0], res[1] - res[0] + 1);

    }
};
