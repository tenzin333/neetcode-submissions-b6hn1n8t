class Solution {
    /**
     * @param {string} s
     * @param {number} k
     * @return {number}
     */
    characterReplacement(s, k) {
        let l=0;
        let maxCount = 0;
        let freq = new Map();

        let maxLen = 0;

        for(let r=0;r<s.length;r++){
            let char = s[r];
            freq.set(char,(freq.get(char) || 0)+1);

            maxCount = Math.max(maxCount,freq.get(char));


            while((r-l+1)-maxCount >k){
                freq.set(s[l],freq.get(s[l])-1);
                l++;
            }

            maxLen = Math.max(maxLen,(r-l+1));
        
        }
        return maxLen;
    }
}
