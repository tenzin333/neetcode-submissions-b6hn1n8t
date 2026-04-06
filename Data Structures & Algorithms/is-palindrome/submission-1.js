class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isPalindrome(s) {
        s= s.toUpperCase();
        const len = s.length;
        let t ="";
        
        for(let i=len-1;i>=0;i--){
            const charCode =s.charAt(i);
            if((charCode>= '0' && charCode <='9')
                || (charCode>='A' && charCode<='Z')
            ) {
                t+=charCode;
            }
        }

        let filtered = '';
           for(let i=0;i<len;i++){
            const charCode =s.charAt(i);
            if((charCode>= '0' && charCode <='9')
                || (charCode>='A' && charCode<='Z')
            ) {
                filtered+=charCode;
            }
        }

        return t==filtered;


    }
}
