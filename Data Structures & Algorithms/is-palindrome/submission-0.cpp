class Solution {
public:
    bool isPalindrome(string s) {
            string temp="";
            for(char c :s){
                if(isalnum(c)){

                        temp+=tolower(c);
                }
            }
            
            string temp2 = temp;
            reverse(temp.begin(),temp.end());
            if(temp==temp2)
                return true;
           
        return false;
    }
};
