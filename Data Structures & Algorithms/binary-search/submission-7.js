class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number}
     */
     binarySearch(left,right,nums,target){
        if(left>right) return -1;

        let mid = left + Math.floor((right-left)/2); //for inter value

        if(nums[mid] == target) return mid;
        return nums[mid] < target ? 
         this.binarySearch(mid+1,right,nums,target)
         : this.binarySearch(0,mid-1,nums,target);  
    }

    search(nums, target) {
        return this.binarySearch(0,nums.length-1,nums,target);
    }

   
}
