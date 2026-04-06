class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    findMin(nums) {
        let minVal = nums[0];
        for(let num of nums){
            if(num<minVal){
                minVal = num;
            }
        }
        return minVal;
    }
}
