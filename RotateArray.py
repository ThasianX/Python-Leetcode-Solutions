from typing import List

# In place solution
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)

        start_i = rotated_count = 0

        while rotated_count < n:
          curr_i = start_i
          prev_num = nums[start_i]

          while True:
            next_i = (curr_i + k) % n
            nums[next_i], prev_num = prev_num, nums[next_i]

            curr_i = next_i
            rotated_count += 1

            if (start_i == curr_i):
              break
          
          start_i += 1
          

tests = [
  (
    ([1,2,3,4,5,6,7], 3),
    [5,6,7,1,2,3,4],
  ),
  (
    ([-1,-100,3,99], 2),
    [3,99,-1,-100],
  ),
]

def validator(rotate, inputs, expected):
    nums, k = inputs

    rotate(nums, k)

    assert len(nums) == len(expected), (len(nums), len(expected))
    assert nums == expected, (nums, expected)

# # Brute force solution
# class Solution:
#     def rotate(self, nums: List[int], k: int) -> None:
#         original = nums.copy()
#         length = len(nums)

#         for i in range(length):
#           nums[(i + k) % length] = original[i]

# tests = [
#   (
#     ([1,2,3,4,5,6,7], 3),
#     [5,6,7,1,2,3,4],
#   ),
#   (
#     ([-1,-100,3,99], 2),
#     [3,99,-1,-100],
#   ),
# ]

# def validator(rotate, inputs, expected):
#     nums, k = inputs

#     rotate(nums, k)

#     assert len(nums) == len(expected), (len(nums), len(expected))
#     assert nums == expected, (nums, expected)