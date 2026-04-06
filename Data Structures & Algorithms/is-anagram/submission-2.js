class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        const slen = s.length;
        const tlen = t.length;

        if(slen!=tlen) return false;
        return s.split('').sort().join('')==t.split('').sort().join('');

    }
}
