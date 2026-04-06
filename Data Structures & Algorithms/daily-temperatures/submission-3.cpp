class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temp) {
      
      vector<int> res(temp.size(),0);
      stack<pair<int,int>> s;

      for(int i=0;i<temp.size();i++){
         int currTemp = temp[i];
         while(!s.empty() && currTemp>s.top().first){
            auto [temp,index] = s.top();
            s.pop();
            res[index] = i-index;
         }
         s.push({currTemp,i});
      }

      return res;
    }
};
