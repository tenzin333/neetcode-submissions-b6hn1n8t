// class Solution {
//     /**
//      * @param {number[]} nums
//      * @param {number} target
//      * @return {number[]}
//      */
//     twoSum(nums, target) {
//         const size = nums.length;
//        for(let i=0;i<size;i++) {
//         for(let j=i+1;j<size;j++){
//             if(nums[i]+nums[j]==target)
//                     return [i,j];
//         }
//        }
//     }
// }


class Solution {
     
     twoSum(nums,target){
        const size= nums.length;
        const map = new Map();
        let result = null;
        
        nums.forEach((num,index) => {
            const diff = target-num;
            if(map.has(diff) && result==null){
                result =  [index,map.get(diff)];
            }
            map.set(num,index);
        })
    return result;
     }
}