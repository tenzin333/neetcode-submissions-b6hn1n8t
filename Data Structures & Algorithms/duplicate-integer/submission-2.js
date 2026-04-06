class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        let size = nums.length;
        const set = new Set();
        for(let i=0;i<size;i++){
            if(set.has(nums[i]))
                return true;
            set.add(nums[i]);
        }
        return false;
    }


}
