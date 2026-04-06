// class Solution {
//     /**
//      * @param {number[]} nums
//      * @return {boolean}
//      */
//     hasDuplicate(nums) {
//         const size = nums.length;
//         for(let i=0;i<size;i++){
//             for(let j=i+1;j<size;j++){
//                 if(nums[i]==nums[j])
//                     return true;
//             }
//         }
//         return false;
//     }

// }

class Solution {
    hasDuplicate(nums){
        const set = new Set();
        for(const num of nums){ 
                if(set.has(num)) return true;
                set.add(num);
        }
        return false;
    }
}