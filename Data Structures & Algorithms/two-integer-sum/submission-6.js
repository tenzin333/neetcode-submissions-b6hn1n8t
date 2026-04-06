class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        let freq = new Map()
        
       for(let i=0; i< nums.length;i++){
           let diff = target - nums[i];
           if(freq.has(diff)){
              let j = freq.get(diff)
              return [i,j]
           }else{
            freq.set(nums[i], i)
           }
       }
    }
}
