from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
      n = len(height)
      left_i = 0
      right_i = n - 1
      max_area = 0

      while left_i < right_i:
        left_height = height[left_i]
        right_height = height[right_i]
        max_area = max(max_area, (right_i - left_i) * min(left_height, right_height))
        
        if left_height < right_height:
          left_i += 1
        else:
          right_i -= 1

      return max_area

tests = [
  (
    ([1,8,6,2,5,4,8,3,7],),
    49,
  ),
  (
    ([1,1],),
    1,
  ),
]