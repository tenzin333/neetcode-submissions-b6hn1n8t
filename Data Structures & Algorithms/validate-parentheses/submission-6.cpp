class Solution {
public:
    bool isValid(string s) {
            unordered_map<char,char> parens;
            parens = {
                {'}','{'},
                {')','('},
                {']','['},
            };

            stack<char> stack;
            for(char c:s){
                if(parens.find(c)!=parens.end()){
                     if(stack.empty()){
                        return false;
                    }else if(stack.top()==parens[c]){
                        stack.pop();
                    }else{
                        return false;
                    }

                }else{
                    stack.push(c);

                }
            }
        
        return stack.empty();
    }
};
