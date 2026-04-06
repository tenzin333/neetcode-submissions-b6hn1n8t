class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    maxSlidingWindow(nums, k) {
        let res = [];
        let l = 0;
        let r = 0;
        while (r < nums.length) {
            if ((r - l + 1) == k) {
                let windowMax = nums[l];
                for (let i = l; i <= r; i++) {
                    windowMax = Math.max(windowMax, nums[i]);
                }
                res.push(windowMax);
                l++;
            }
            r++;
        }
        return res;
    }
}
