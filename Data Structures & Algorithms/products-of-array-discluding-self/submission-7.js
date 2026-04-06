class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    productExceptSelf(nums) {
        const size = nums.length;
        const result = Array(nums.length).fill(1);

        //pass 1
        let prefix = 1
        for(let i=0;i<size;i++){
            result[i] = prefix;
            prefix *=nums[i]; 
        }

        //pass 2
        let suffix =1;
        for(let i=size-1;i>=0;i--){
            result[i]*=suffix;
            suffix*=nums[i];
        }

        return result;

    }
}
