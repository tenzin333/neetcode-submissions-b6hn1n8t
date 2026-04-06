class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        const s_size = s.length;
        const t_size = t.length;
        const Smap = new Map();
         const Tmap = new Map();
        if(s_size!=t_size)  return false;
        return s.split('').sort().join()==t.split('').sort().join();
    }
}
