class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {
        const size = nums.length;
        const frequencyMap = new Map();
        for (let num of nums) {
            frequencyMap.set(num, (frequencyMap.get(num) || 0) + 1);
        }

        //create bucket
        const bucket = Array(nums.length+1).fill(null).map(() => []);
        frequencyMap.forEach((freq,num) => {
            bucket[freq].push(num);
        })

        const result = [];
        for(let i=bucket.length-1;i>=0 && result.length<k ; i--){
            if(bucket[i].length>0){
                result.push(...bucket[i]);
            }
        }

        return result;

       
    }
}
