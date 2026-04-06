class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {
        let freq = new Map();

        for(let i of nums){
            freq.set(i, (freq.get(i) || 0) +1);
        }

        //lets create a bucket [index=frequency]
        const bucket = new Array(nums.length+1).fill(null)
            .map(() => []);

        for(let [key,count] of freq){
              bucket[count].push(key);
        }

        let result = [];
        for(let i=bucket.length-1; i>=0 && result.length<k;i--){
            for(let c of bucket[i]){
                result.push(c);
            }
            if(result.length==k) break;
        }

        return result;

    }
}
