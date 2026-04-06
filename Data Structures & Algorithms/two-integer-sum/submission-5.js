class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        const size = nums.length;
        const map = new Map();
        for(let i=0;i<size;i++){
            if(map.has(nums[i])){
                return [map.get(nums[i]),i];
            }
            const diff = target-nums[i];
            map.set(diff, i);
        }
        return [];
    }
}
