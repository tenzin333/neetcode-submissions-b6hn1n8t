class Solution {
    /**
     * @param {number[]} nums
     * @return {number[][]}
     */
    threeSum(nums) {
        const size = nums.length;
        if(size===0) return [];
        const result = [];
        nums.sort((a,b) => a-b);
        for(let i=0;i<size-2;i++){
            if(i>0 && nums[i]==nums[i-1])   continue; // skip duplicate

            let left = i+1;
            let right = size-1;

            while(left<right){
                const sum = nums[left]+nums[right]+nums[i];
                if(sum===0) {
                    result.push([nums[i],nums[left],nums[right]]);

                    while(left < right && nums[left]==nums[left+1]) left++;
                    while(left < right && nums[right]==nums[right-1]) right--;
                    left++;
                    right--;
                }else if(sum>0){
                     right-=1;
                }else{
                    left+=1;
                }
            }
        }
        return result;
    }
}
