class Solution {
    /**
     * @param {number[]} prices
     * @return {number}
     */
    maxProfit(prices) {
        let buy = Infinity;
        let profit = 0;

        for(let price of prices){
           if(buy < price){
            profit = Math.max(profit, price - buy);
           }else{
            buy  = price;
           }
        }
        return profit;

    }
}
