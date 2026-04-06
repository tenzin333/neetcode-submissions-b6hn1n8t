class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    productExceptSelf(nums) {
        const size = nums.length;
        const result = [];

        for(let i=0;i<size;i++){
            let product = 1;
            for(let j=0;j<size;j++){
              if(i!=j){
                product*=nums[j];
              }
            }
            result[i] = product;
        }
        return result;
    }
}
