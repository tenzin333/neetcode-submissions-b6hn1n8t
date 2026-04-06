class Solution {
    /**
     * @param {number[]} nums1
     * @param {number[]} nums2
     * @return {number}
     */
    findMedianSortedArrays(nums1, nums2) {
        let A = nums1;
        let B = nums2;

        let total = nums1.length + nums2.length;
        let half = Math.floor((total+1)/2);

        if(B.length < A.length){
            [A,B] = [B,A];
        }
        let l=0,r=A.length;

        while(l<=r){
            let i=Math.floor((l+r)/2); //no of elemnts from A
            let j =half-i;  // no of elements from B

            let Aleft = i>0 ? A[i-1]:Number.MIN_SAFE_INTEGER;
            let Aright= i<A.length ? A[i]:Number.MAX_SAFE_INTEGER;

            let Bleft = j>0 ? B[j-1]:Number.MIN_SAFE_INTEGER;
            let Bright= j<B.length ? B[j]: Number.MAX_SAFE_INTEGER;

            if(Aleft<=Bright && Bleft<=Aright){
                if(total%2!=0){
                    return Math.max(Aleft,Bleft);
                }else{
                    return (Math.max(Aleft,Bleft) + Math.min(Aright,Bright))/2;
                }
            }else if(Aleft > Bright){
                r = i-1;
            }else {
                 l= i+1;
            }
            
            }
        return -1;
    }
}
