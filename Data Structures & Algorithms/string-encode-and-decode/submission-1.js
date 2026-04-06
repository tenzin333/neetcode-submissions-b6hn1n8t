let secret = "#"

class Solution {
    /**
     * @param {string[]} strs
     * @returns {string}
     */
    
    encode(strs) {
        let new_str=""
        for(let str of strs){
            let n = str.length;
            new_str += `${n}${secret}${str}`
        }
        return new_str
    }

    /**
     * @param {string} str
     * @returns {string[]}
     */
    decode(str) {
        if(str.length==0) return []

        let left  = 0;
        let res = []
        while(left < str.length){
            let j = left;
            while(str[j]!="#"){
                j++
            }
            let word_len = Number(str.slice(left,j))
            let sliced = str.slice(j+1, j+1+word_len)
            res.push(sliced)
            left =  j+1 + word_len
        }

        return res

    }
}
