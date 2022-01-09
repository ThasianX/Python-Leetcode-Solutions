from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
      n = len(numbers)
      l, r = 0, n - 1

      while l < r:
        total = numbers[l] + numbers[r]
        if total == target:
          return [l + 1, r + 1]
        elif total < target:
          l += 1
        else:
          r -= 1

      return [0, 0]
        

tests = [
  (
    ([2,7,11,15],9,),
    [1,2],
  ),
  (
    ([2,3,4],6,),
    [1,3],
  ),
  (
    ([-1,0],-1,),
    [1,2],
  ),
  (
    ([-100,20,40,100],-60,),
    [1,3],
  ),
]