class Solution {
    /**
     * @param {string} s
     * @return {number}
     */
    lengthOfLongestSubstring(s) {
        let output=0;
        let set = new Set();
        for(let i=0;i<s.length;i++){
            let count = 1;
            set.add(s.charAt(i));
            for(let j=i+1;j<s.length;j++){
                    if(set.has(s.charAt(j))){
                        set.clear();
                        break;
                    }else{
                        set.add(s.charAt(j));
                        count++;
                    }
            }
            output = Math.max(output,count);
        }
        return output;
    }
   
}
