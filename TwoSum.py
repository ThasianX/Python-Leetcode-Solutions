from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      complements = {}

      for i in range(len(nums)):
        complement = target - nums[i]
        if complement in complements:
          return [complements[complement], i]
        complements[nums[i]] = i

      return [-1, -1]

        
tests = [
  (
    ([2,7,11,15],9,),
    [0,1],
  ),
  (
    ([3,2,4],6,),
    [1,2],
  ),
  (
    ([3,3],6,),
    [0,1],
  ),
]