"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example 1:

Input: [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
             Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Example 2:

Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.
Example 3:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        isbuy=False
        buyPrice=0
        sellPrice=0
        profit=0
        if len(prices) in [0,1]:
            return 0
        elif prices[0]<=prices[1]:
            isbuy=True
            buyPrice=prices[0]
        for i in range(1,len(prices)-1):  
            if (prices[i-1]<=prices[i]) and (prices[i+1]<=prices[i]) and (isbuy):
                isbuy=False
                sellPrice=prices[i]
                profit+=(sellPrice-buyPrice)
            elif (prices[i-1]>=prices[i]) and (prices[i+1]>=prices[i]) and (not isbuy):
                isbuy=True
                buyPrice=prices[i]
        if prices[len(prices)-2]<=prices[len(prices)-1] and (isbuy):
            isbuy=False
            sellPrice=prices[len(prices)-1]
            profit+=(sellPrice-buyPrice)
        return profit

"""
Runtime: 64 ms, faster than 80.83% of Python3 online submissions for Best Time to Buy and Sell Stock II.
Memory Usage: 13.8 MB, less than 82.93% of Python3 online submissions for Best Time to Buy and Sell Stock II.
"""
