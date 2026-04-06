class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    maxSlidingWindow(nums, k) {
        const res = [];
        let l=0;
        for(let r=0;r<nums.length;r++){
            let max = nums[r];
            if((r-l+1) == k){
                for(let i=l;i<=r;i++){
                     max = Math.max(max,nums[i]);
                }
                res.push(max);
                l++;
            }
        }
        return res;
    }
}
