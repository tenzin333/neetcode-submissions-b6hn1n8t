class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    productExceptSelf(nums) {
        const result = [];
        const size = nums.length;
        for(let i=0;i<size;i++){
           let output = 1;
           for(let j=0;j<size;j++){
            if(i!=j){
                output*=nums[j];
            }
           }
            result.push(output);
        }
        return result;
    }
}
