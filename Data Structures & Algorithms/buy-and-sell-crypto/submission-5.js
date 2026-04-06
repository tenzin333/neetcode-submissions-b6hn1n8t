class Solution {
    /**
     * @param {number[]} prices
     * @return {number}
     */
    maxProfit(prices) {
        let profit = 0;

        for(let i=0;i<prices.length-1;i++){
            const buy = prices[i];
            for (let j=i+1;j<prices.length;j++){
                if(buy<prices[j]){
                    profit = Math.max(profit,prices[j]-buy);
                }
            }
        }
        return profit;
    }
}
