class Solution {
    /**
     * @param {number[]} nums
     * @return {number[][]}
     */
    threeSum(nums) {
        const size = nums.length;
        const res = [];
        nums.sort((a,b) => a-b);

        for(let i=0;i<size-2;i++){
            if(i>0 && nums[i]==nums[i-1]) continue;
            let left = i+1;
            let right = size-1;
            while(left<right){
                const sum = nums[left]+nums[right]+nums[i];
                if(sum==0){
                    res.push([nums[i],nums[left],nums[right]]);

                    while(left<right && nums[left]==nums[left+1]) left+=1;
                    while(left<right && nums[right]==nums[right-1]) right-=1;
                    left++;
                    right--;
                }else if(sum>0){
                    right--;
                }else{
                    left++;
                }

            }
        }
        
            return res;
    }
}
