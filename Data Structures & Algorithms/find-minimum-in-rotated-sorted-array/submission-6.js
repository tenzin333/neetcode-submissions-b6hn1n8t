class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    findMin(nums) {
        //since is its sorted  i can apply BS and extract the right half of the array
        // and get min from there


        let left =0 ;
        let right = nums.length-1;

        while(left<right){
                let mid = left + Math.floor((right-left)/2);
                if(nums[mid] > nums[right]){
                    left= mid+1;
                }else{
                    right = mid;
                }
        }
        return nums[left];
    }
}
