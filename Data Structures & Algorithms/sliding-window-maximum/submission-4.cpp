class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
            int l=0,r=0;
            int Max = INT_MIN;
            vector<int> res;    
            while(r<nums.size()){
                Max = max(Max,nums[r]);
             
                if((r-l+1)==k){
                    // cout<<true<<endl;
                    res.push_back(Max);
                    Max=INT_MIN;
                    r=l;
                    l+=1;

                }
                r++;
            }
   

            return res;
   
   
    }  
};
