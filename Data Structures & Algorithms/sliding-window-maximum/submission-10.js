class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    maxSlidingWindow(nums, k) {
        let q =new Deque();
        let l=0,
            r=0;
        let output = [];

        while(r<nums.length){

            while(q.size() && nums[q.back()] < nums[r]){
                    q.popBack();
            }
            q.pushBack(r);

            if(l>q.front()){
                q.popFront();
            }

            if(r+1>=k){
                output[l] = nums[q.front()];
                l++;
            }
            r++;
        }
        return output;

    }
}
