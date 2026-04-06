class Solution {
public:
    int search(vector<int>& nums, int target) {
            if(nums.size()==0){
                return -1;
            }
            int index = binarySearch(nums,0,nums.size()-1,target);
            return index;
    }

private:
    // int binarySearch(vector<int>& nums,int start,int end,int target){
    //                 int mid = start+(end-start)/2;

    //                 if(nums[mid]==target)
    //                         return mid;

    //                 if(nums[mid-1]>target){
    //                     binarySearch(nums,0,mid-1,target);
    //                 }else {
    //                     binarySearch(nums,mid,nums.size()-1,target);
    //                 }

    //                 return -1;
    // }

    int binarySearch(vector<int> nums,int start,int end,int target){
            while(start<=end){
                // int mid = start+(end-start)/2;
                int mid = start + (end - start) / 2;
                if(nums[mid]==target){
                    return mid;
                }
                if(nums[mid]>target){
                    end = mid-1;
                }else{
                    start= mid+1;
                }
            }

            return -1;
    }
};
