class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    longestConsecutive(nums) {
        let seen = new Set(nums)
        let maxLen = 0;

        for(let num of nums){
            if(!seen.has(num-1)){
                let curr = num
                let len = 1
                while(seen.has(curr+1)){
                    curr++
                    len++
                }
                maxLen = Math.max(len, maxLen)
            }
        }
        return maxLen
    }
}
