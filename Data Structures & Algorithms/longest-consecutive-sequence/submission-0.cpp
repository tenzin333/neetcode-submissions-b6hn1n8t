class Solution {
public:
    int longestConsecutive(vector<int>& nums) {

        set<int> mySet;

        for(int i=0;i<nums.size();i++){
            mySet.insert(nums[i]);
        }

        int length=0;
        int finalLength=0;
        for(int i=0;i<nums.size();i++){
            length =1;
            if(mySet.find(nums[i]-1)!=mySet.end()){
                    length ++;
                    while(mySet.find(nums[i]-length)!=mySet.end()){
                        length++;
                    }
                    finalLength = max(length,finalLength);
                 
                    
            }else{
                finalLength = max(length,finalLength);
            }
        }
        return finalLength;
    }
};

