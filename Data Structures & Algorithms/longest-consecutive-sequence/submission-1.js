class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    longestConsecutive(nums) {
        const size = nums.length;
        if(size===0) return 0;
        const numSet = new Set(nums);

        let count=1;
        for(let num of numSet){
                if(!numSet.has(num-1)){
                    let current = num;
                    let  tempCount=1; 
                       while(numSet.has(current+1)){
                        tempCount++;
                        current ++;
                       }
                       count = Math.max(count,tempCount);
                }

        }
       return count;
    }
}
