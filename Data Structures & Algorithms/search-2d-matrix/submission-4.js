class Solution {
    binary_search(left, right, nums, target) {
        if (left > right) return false;

        let mid = left + Math.floor((right - left) / 2);

        if (nums[mid] === target) {
            return true;
        }

        return nums[mid] > target
            ? this.binary_search(left, mid - 1, nums, target)
            : this.binary_search(mid + 1, right, nums, target);
    }

    searchMatrix(matrix, target) {
        const m = matrix.length;
        const n = matrix[0].length;

        for (let i = 0; i < m; i++) {
            if (this.binary_search(0, n - 1, matrix[i], target)) {
                return true;
            }
        }
        return false;
    }
}
