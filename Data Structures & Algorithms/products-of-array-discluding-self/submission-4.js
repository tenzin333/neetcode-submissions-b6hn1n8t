class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    productExceptSelf(nums) {
        const result = [];
        const size = nums.length;
        const leftProduct = [];
        const rightProduct = [];
        
        let tempLeft = 1;
        for(let i=0;i<size;i++){
            leftProduct[i] = tempLeft;
            tempLeft *= nums[i]; 
        }

         let tempRight = 1;
        for(let j=size-1;j>=0;j--){
            rightProduct[j] = tempRight;
            tempRight *= nums[j]; 
        }

        for(let i=0;i<size;i++){
            result[i] = leftProduct[i]*rightProduct[i];
        }

        return result;
    }
}
