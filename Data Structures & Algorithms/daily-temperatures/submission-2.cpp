class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temp) {
        int l=0;
        int r=1;
        vector<int> res(temp.size(),0); 
        while(r<temp.size()){
            // cout<<temp[l]<<temp[r]<<endl;
           if(l!=r && temp[l]<temp[r]){
            // cout<<temp[r]<<endl;
              res[l]= (r-l);
              r=l;
              l++;
           }else if(r==(temp.size()-1) && l<r){
               r=l;
               l++;
           }
            r++;
         }
         return res;
    }
};
