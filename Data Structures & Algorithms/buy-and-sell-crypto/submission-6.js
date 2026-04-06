class Solution {
    /**
     * @param {number[]} prices
     * @return {number}
     */
    maxProfit(prices) {
            let minPrice = Infinity;
            let maxProfit = 0;

            for(let p of prices){
                if(p<minPrice){
                    minPrice = p;
                }else{
                    maxProfit = Math.max(maxProfit,p-minPrice);
                }
            }

        return maxProfit;
    }
}
