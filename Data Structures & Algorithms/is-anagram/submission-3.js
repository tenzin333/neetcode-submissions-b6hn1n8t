class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        const slen = s.length;
        const tlen = t.length;
        const tempS = s.toLowerCase();
        const tempT = t.toLowerCase();
        if(tlen!=slen) return false;

        let charArray = new Array(26).fill(0);
        for(let i=0;i<slen;i++){
            charArray[tempS.charCodeAt(i) - 97]++;
            charArray[tempT.charCodeAt(i) - 97]--;
        }
        return charArray.every(c => c==0);

    }
}
