class Solution {
    /**
     * @param {number[]} prices
     * @return {number}
     */
    maxProfit(prices) {
        let buy = 0,sell=0;
        let profit = 0;
        for(let i=0;i<prices.length;i++){
            buy = prices[i]; //1
            for(let j=i+1;j<prices.length;j++){
                   sell = prices[j]; 
                   if(sell > buy) { 
                        profit = Math.max(profit, sell-buy); 
                    
                   }
                 
            }
        }
        return profit;
    }
}
