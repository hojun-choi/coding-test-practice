"""
Problem: Best Time to Buy and Sell Stock
Difficulty: Easy
Category: Array / String / Hash
Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

Study Plan:
- Week: 1
- Day: 2
- Role: Practice
- Task:
  - Track running minimum and best profit.

Idea:
- 이중루프 돌기

Code:
  '''
  class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        len_prices = len(prices)
        output = 0
        for n in range(len_prices):
            buy = prices[n]
            for n2 in range(n+1, len_prices):
                if prices[n2] > output + buy:
                    output = prices[n2]-buy

        return output
  '''

Time Complexity:
- O(n^2) where n is the length of the input list.

Space Complexity:
- O(1) as we are not using any additional data structures.

Status:
- Solved

Mistake:
- None yet.

Retry:
  Idea:
  - 최소값 최대값을 저장하는게 아닌 최소값과 최대이익을 저장하기.

  Code:
    '''
    class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0

        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)

        return max_profit
    '''

  Time Complexity:
  - O(n) where n is the length of the input list.

  Space Complexity:
  - O(1) as we are using only a constant amount of extra space.
"""
