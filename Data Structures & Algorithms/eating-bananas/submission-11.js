class Solution {
    /**
     * @param {number[]} piles
     * @param {number} h
     * @return {number}
     */
    minEatingSpeed(piles, h) {

        let left = 0;
        let right = Math.max(...piles);

        while (left < right) {
            let k = left + Math.floor((right - left) / 2);
            let hrs = 0;
            for (let pile of piles) {
                hrs += Math.ceil(pile / k);
            }

            if (hrs <= h) {
                right = k;
            } else {
                left = k + 1;
            }
        }
        return left;
    }
}
