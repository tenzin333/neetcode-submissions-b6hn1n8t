class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {
        
        let freq = new Map()

        for(let n of nums){
            freq.set(n, (freq.get(n) || 0) + 1)
        }

        return [...freq.entries()]
            .sort((a,b) => b[1] - a[1])
            .slice(0,k)
            .map((x) => x[0])

       
    }

}
