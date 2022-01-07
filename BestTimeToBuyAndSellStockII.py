from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        totalProfit = 0

        for i in range(len(prices) - 1):
          localProfit = prices[i + 1] - prices[i]
          if localProfit > 0:
            totalProfit += localProfit

        return totalProfit

tests = [
  (
    ([7,1,5,3,6,4],),
    7,
  ),
  (
    ([1,2,3,4,5],),
    4,
  ),
  (
    ([7,6,4,3,1],),
    0,
  ),
  (
    ([1],),
    0,
  )
]