class Solution {
    /**
     * @param {number[]} nums1
     * @param {number[]} nums2
     * @return {number}
     */
    findMedianSortedArrays(nums1, nums2) {
        let m = nums1.length;
        let n = nums2.length;
        let i=0;
        let j=0;
        let arr = [];
        while(i<m && j<n){
            if(nums1[i] <= nums2[j]){
                arr.push(nums1[i]);
                i++;
            }else{
            arr.push(nums2[j]);
            j++;
            }
        }

        if(j<n){
            arr.push(...nums2.slice(j,n));
        }
        
        if(i<m){
            arr.push(...nums1.slice(i,m));
        }

        if(arr.length%2 !=0){
            let mid = Math.floor(arr.length/2);
            return arr[mid];
        }else{
            let mid = Math.floor(arr.length/2);
            return (arr[mid]+arr[mid-1])/2;
        }
    }
}
