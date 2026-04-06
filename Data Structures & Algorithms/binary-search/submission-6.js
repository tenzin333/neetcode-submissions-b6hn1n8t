class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number}
     */
    search(nums, target) {
        let left = 0, right = nums.length - 1;
        while (left <= right) {
            if (nums[left] === target) return left;
            if (nums[right] === target) return right;
            left++;
            right--;
        }
        return -1;
    }
}
