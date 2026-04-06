// class Solution {
//     /**
//      * @param {string} s
//      * @param {string} t
//      * @return {boolean}
//      */
//     isAnagram(s, t) {
//         const s_size = s.length;
//         const t_size = t.length;
//         const Smap = new Map();
//          const Tmap = new Map();
//         if(s_size!=t_size)  return false;
//         return s.split('').sort().join()==t.split('').sort().join();
//     }
// }


class Solution {
    isAnagram(s,t){
        const count = new Map();
        if(s.length!=t.length) return false;
       
        for(const c of s){
            count.set(c,(count.get(c) || 0) +1);
        }

        for(const c of t){
            if(!count.has(c)) return false;
            count.set(c,count.get(c)-1);
            if(count.get(c)<0)  return false;
        }
        return true;
    }
}