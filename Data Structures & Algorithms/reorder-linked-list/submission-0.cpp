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

// class Solution {
// public:
//     void reorderList(ListNode* head) {
//         vector<ListNode*> nodes;
//         ListNode *current = head;
//          while(current!=NULL){
//             nodes.push_back(current);
//             current=current->next;
//          }

//          int n = nodes.size();
//          int l=0;
//          int r = n-1;
//          while(l<r){
//             nodes[l]->next = nodes[r];
//             l++;
//             if(l==r)    break;
//             nodes[r]->next = nodes[l];
//             r--;
//          }
//          nodes[l]->next = NULL;

//     }
// };

class Solution{
    public: 
        void reorderList(ListNode* head){
           
            /*
                1) find the middle of LL using slow and fast approach
                2) reverse the second half
                3) merge both
            */
           
            ListNode *slow  = head;
            ListNode *fast = head;

            while(fast!=NULL && fast->next !=NULL){
                slow = slow->next;
                fast = fast->next->next;
            }

            ListNode *curr = slow;
            ListNode *prev = NULL;

            while(curr!=NULL){  //reverse of second  half
                    ListNode *nextTemp = curr->next;
                    curr->next = prev;
                    prev = curr;
                    curr = nextTemp;
            }
         
           ListNode *first = head;

           ListNode *second = prev;
          
           while(second->next!=NULL){
            ListNode *temp1 = first->next;
            ListNode *temp2 = second->next;

            first->next = second;
            second->next = temp1;
            first=temp1;
            second = temp2;
           }

        }
};
