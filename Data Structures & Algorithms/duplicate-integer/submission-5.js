class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
            const len = nums.length;
            for(let i=0;i<len;i++){
                for(let j=0;j<len;j++){
                    if(i!=j && nums[i]==nums[j]){
                        return true;
                    }
                }
            }
        return false;
    }
}
