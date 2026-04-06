class Solution {
    groupAnagrams(strs){
        const map = new Map();

        for(const chars of strs){
            const sortedStr = chars.split("").sort().join();
            if(!map.has(sortedStr)) map.set(sortedStr,[]);
            map.get(sortedStr).push(chars);
        }

        const result=[];
        for(const groups of map.values()){
            result.push(groups);
        }
        return result;
    }
}