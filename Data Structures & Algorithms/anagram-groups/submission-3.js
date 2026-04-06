class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        let freq = new Map();

        for(let str of strs){
            let sorted_str = str.split('').sort().join('');

            freq.set(sorted_str, [...(freq.get(sorted_str) || []), str])
        }

        return [...freq.values()]
    }
}
