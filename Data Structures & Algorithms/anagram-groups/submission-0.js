class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        const map = new Map();

        for (const str of strs) {
            const sortedStr = str.split("").sort().join(""); // Use '' not ','
            if (!map.has(sortedStr)) {
                map.set(sortedStr, []);
            }
            map.get(sortedStr).push(str); // Use get, not set().push()
        }

        const result = [];
        for (const group of map.values()) {
            result.push(group);
        }

        return result;
    }
}
