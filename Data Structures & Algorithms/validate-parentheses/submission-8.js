class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isValid(s) {
            const stack = [];

            const map = {
                ')':'(',
                ']':'[',
                '}':'{'
            }

            if(s.length %2 !=0) return false;

            for(let i=0;i<s.length;i++){
                const char = s.charAt(i);    
                if(char === '[' || char=='(' || char=='{'){
                    stack.push(char);
                }else{
                    if(stack[stack.length-1] != map[char]){
                            return false;
                    }
                    stack.pop(); //remove top
                }
            }

            return stack.length==0;

    }
}
