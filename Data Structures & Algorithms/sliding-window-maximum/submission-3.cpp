class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
            int l=0;
            int r=0;
            vector<int> res;
            int max = INT_MIN;
            while(r<nums.size()){
                if(nums[r]>max){
                    max = nums[r];
                }
                if((r-l+1)==k){
                    res.push_back(max);
                    r=l;
                    l++;
                    max=INT_MIN;
                    
                   
                }   
               
                r++;
            }

        return res;
    }
};
