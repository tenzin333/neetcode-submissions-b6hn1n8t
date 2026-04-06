class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        stack<pair<int,int>> s;
        int maxArea = 0;

        for(int i=0;i<heights.size();i++){
            int start = i;
            while(!s.empty() && s.top().second > heights[i]){
                  pair<int,int> top = s.top();
                  int index = top.first;
                  int height = top.second;
                  s.pop();
                  start = index;
                  maxArea = max(maxArea, (height*(i-index)));
            }
            s.push({start,heights[i]});
           
        }

         while(!s.empty()){
                    int index = s.top().first;
                    int height = s.top().second;
                    
                    maxArea = max(maxArea,(height* (static_cast<int> (heights.size()-index)))); 

                    s.pop();
            }


        return maxArea;
    }
};
