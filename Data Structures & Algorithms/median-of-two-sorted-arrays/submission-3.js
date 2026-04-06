class Solution {
    /**
     * @param {number[]} nums1
     * @param {number[]} nums2
     * @return {number}
     */
    findMedianSortedArrays(nums1, nums2) {
        const m = nums1.length;
        const n = nums2.length;
        let arr = [];
        let i=0;
        let j=0;
        while(i<m && j<n){
            if(nums1[i] < nums2[j]){
                arr.push(nums1[i]);
                i++;
            }else{
                arr.push(nums2[j]);
                j++;
            }
        }

        if(i<m){
            arr.push(...nums1.slice(i,m));
        }

        if(j<n){
             arr.push(...nums2.slice(j,n));   
        }
        
        if(arr.length %2 !=0){
            return arr[Math.floor(arr.length/2)];
        }else{
            const mid = Math.floor(arr.length/2);
            const a = arr[mid-1];
            const b = arr[mid];
            return (a+b)/2;
        }
    }


}
