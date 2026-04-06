class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    longestConsecutive(nums) {
        let maxLen = 0;
        let seen = new Set(nums);
        
        for(let i=0;i<nums.length;i++){
           if(!seen.has(nums[i]-1)){
                let len = 1;
                let curr = nums[i];

                while(seen.has(curr+1)){
                    curr++;
                    len++;
                }
                maxLen = Math.max(len,maxLen);
           }
        }
        return maxLen;
    }
}
