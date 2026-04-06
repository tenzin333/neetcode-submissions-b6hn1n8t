class Solution {
    /**
     * @param {number[]} piles
     * @param {number} h
     * @return {number}
     */
    minEatingSpeed(piles, h) {
        //applying BS on  K = [1.....MAX(PILE)]
        let left = 0;
        let right = Math.max(...piles);

        while(left<right){
            let mid = left + Math.floor((right-left)/2);
            let hrs = 0;
            for(let pile of piles ){
                hrs += Math.ceil(pile/mid);
            }

            if(hrs<=h){
                right = mid;
            }else{
                left = mid+1;
            }
        }
        return left;

    }
}
