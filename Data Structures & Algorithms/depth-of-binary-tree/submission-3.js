/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     constructor(val = 0, left = null, right = null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    /**
     * @param {TreeNode} root
     * @return {number}
     */
    maxDepth(root) {
        if(!root) return 0;
        let q = new Queue([root]);
        let level = 0;
        while(!q.isEmpty()){
            let size = q.size();

            for(let i=0; i<size;i++){
                 let node  = q.pop();
                 if(node.left)  q.push(node.left);
                 if(node.right)  q.push(node.right);
            }
            level++;
        }
        return level;
    }
}
