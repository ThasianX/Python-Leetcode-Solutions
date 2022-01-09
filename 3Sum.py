from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
      n = len(nums)
      triplets = []

      # Input is sorted so we can run a 2 pointer two sum
      nums.sort()

      def twoSumII(i: int):
        l, r = i + 1, n - 1
        # nums[i] + nums[l] + nums[r] = 0
        # -> nums[l] + nums[r] = -nums[i]
        target = -nums[i]
        
        while l < r:
          total = nums[l] + nums[r]
          if total == target:
            triplets.append([nums[i], nums[l], nums[r]])
            # move both left and right pointers toward the center
            # since that specific combination can't be repeated
            # unless it's a duplicate
            l += 1
            r -= 1
            # skip past all duplicates so we don't end up with the
            # same combination we just appended
            while l < r and nums[l] == nums[l - 1]:
              l += 1
          elif total < target:
            l += 1
          else:
            r -= 1

      for i in range(n):
        if nums[i] > 0:
          break
        if i == 0 or nums[i] != nums[i - 1]:
          twoSumII(i)

      return triplets

# No sort
# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#       triplets, dups = set(), set()
#       complement_to_index = {}

#       for (i, num1) in enumerate(nums):
#         if num1 in dups:
#           continue

#         dups.add(num1)
#         for (j, num2) in enumerate(nums[i + 1:]):
#           complement = -num1 - num2
#           if complement in complement_to_index and complement_to_index[complement] == i:
#             triplets.add(tuple(sorted((num1, num2, complement))))
#           complement_to_index[num2] = i
      
#       return list(triplets)
        
tests = [
  (
    ([-1,0,1,2,-1,-4],),
    [[-1,-1,2],[-1,0,1]],
  ),
  (
    ([],),
    [],
  ),
  (
    ([0],),
    [],
  ),
]