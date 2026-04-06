class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    productExceptSelf(nums) {

        let prefixSum = []
        let suffixSum = []

        const x = 1


        let prefix = 1
        for(let i=0;i<nums.length;i++){
            prefixSum[i] = prefix
            prefix *= nums[i]
           
        }

        let suffix = 1
        for(let i = nums.length-1;i>=0;i--){
            suffixSum[i] = suffix;
            suffix *= nums[i]
            
        }

        let result = [];

        for(let i=0;i<nums.length;i++)
            result[i] = prefixSum[i] * suffixSum[i]

        return result;


    }
}
