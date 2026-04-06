/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
            int n = lists.size();

            if(n==0)    return NULL;

            while(n>1){
                for(int i=0;i< n/2 ;i++){
                        lists[i] = mergeLists(lists[i],lists[n-i-1]);
                }       
                n= (n+1)/2;
            }

            return lists.front();
    }


    ListNode* mergeLists(ListNode* l1, ListNode* l2){
        ListNode* dummy = new ListNode();
        ListNode* curr= dummy;
       
        while(l1!=NULL && l2!=NULL){
            if(l1->val<=l2->val){
                curr->next = l1;
                l1  = l1->next;
            }else{
                curr->next = l2;
                l2 = l2->next;
            }
            curr = curr->next;

        }

        if(l1!=NULL){
            curr->next = l1;
        }else{
            curr->next = l2;
        }

        return dummy->next;
    }
};
