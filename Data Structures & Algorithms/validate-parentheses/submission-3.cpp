class Solution {
public:
    bool isValid(string s) {
        stack<int> stack;
        unordered_map<char,char> parens = {
            {')','('},
            {']', '['},
            {'}', '{'},

        };
       
        for(char c:s){
            if(parens.find(c)!=parens.end()){

                    if(stack.empty()){
                        return false;
                    }
                    if(stack.top()!=parens[c]){
                        return false;
                    }
                    stack.pop();
            }else{
                   stack.push(c); 
            }
        }
        return stack.empty();
    }
};
