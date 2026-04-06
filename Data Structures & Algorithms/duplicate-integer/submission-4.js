class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        const set = new Set();
        for (let num of nums) {
            if (set.has(num)) {
                return true;  // This exits the whole function
            }
            set.add(num);
        }
        return false;
    }
}
