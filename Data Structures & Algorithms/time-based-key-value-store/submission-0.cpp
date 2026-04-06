class TimeMap {
private : 
     unordered_map<string,vector<pair<int,string>>> map;  
public:
    TimeMap() {
           
          }
    
    void set(string key, string value, int timestamp) {
            map[key].push_back({timestamp,value});
    }
    
    string get(string key, int timestamp) {
                auto& val = map[key];

                int start = 0;
                int end = val.size()-1;
                string ans = "";
                while(start<=end){
                    int mid = start+(end-start)/2;
                    if(val[mid].first<=timestamp){
                        ans = val[mid].second;
                        start = mid+1;
                    }else{
                        end = mid-1;
                    }
                }
            return ans;
    }
};
