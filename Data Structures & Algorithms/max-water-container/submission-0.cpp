class Solution {
public:
    int maxArea(vector<int>& heights) {
        int left = 0;
        int right = heights.size()-1;

        int curr=0;
        int res =0;
        while(left<right){
            curr = min(heights[left],heights[right])*(right-left);
            res = max(curr,res);
            if(heights[left]<=heights[right]){
                left++;
            }else{
                right--;
            }
        }
        return res;
    }
};
