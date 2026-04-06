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

        let buckets = Array.from({length: nums.length+1}, () => [])

        for(let [num,count] of freq){
            buckets[count].push(num)
        }
        
        let res = []
        for(let i= buckets.length-1; i>=0 && res.length < k; i--){
            res.push(...buckets[i])
        }

        return res.slice(0,k)
    }

}
