from typing import List
from collections import Counter

# sliding window with counter
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
      n = len(fruits)
      max_fruits = 0

      left_i = 0
      fruits_counter = Counter()

      for right_i in range(n):
        fruits_counter[fruits[right_i]] += 1

        # If we have more than 2 fruits, we keep
        # sliding the left index forward and decrementing
        # fruits that it's seen until we fully eliminate
        # a fruit type such that we are back to 2 fruits
        # in our basket
        while len(fruits_counter) > 2:
          left_fruit = fruits[left_i]
          fruits_counter[left_fruit] -= 1
          
          if fruits_counter[left_fruit] == 0:
            fruits_counter.pop(left_fruit)
          left_i += 1
        
        max_fruits = max(max_fruits, right_i - left_i + 1)

      return max_fruits

# # sliding window with set
# class Solution:
#     def totalFruit(self, fruits: List[int]) -> int:
#       n = len(fruits)
#       max_fruits = 0

#       i = 0

#       while i < n:
#         local_fruits = 0
#         seen_fruits = set()

#         if i - 1 >= 0:
#           seen_fruits.add(fruits[i - 1])
#           j = i - 1
#           while j >= 0 and fruits[j] == fruits[i - 1]:
#             local_fruits += 1
#             j -= 1
        
#         while i < n:
#           seen_fruits.add(fruits[i])
#           if len(seen_fruits) > 2:
#             break
#           local_fruits += 1
#           i += 1
        
#         max_fruits = max(max_fruits, local_fruits)

#       return max_fruits

# # brute force
# class Solution:
#     def totalFruit(self, fruits: List[int]) -> int:
#       max_fruits = 0

#       for i in range(len(fruits)):
#         local_fruits = 0
#         seen_fruits = set()
        
#         for fruit in fruits[i:]:
#           seen_fruits.add(fruit)
#           if len(seen_fruits) > 2:
#             break
#           local_fruits += 1
        
#         max_fruits = max(max_fruits, local_fruits)
      
#       return max_fruits

        
tests = [
  (
    ([1,2,1],),
    3,
  ),
  (
    ([0,1,2,2],),
    3,
  ),
  (
    ([1,2,3,2,2],),
    4,
  ),
  (
    ([0],),
    1,
  ),
  (
    ([0,0,0,0,0,0,0,0,0,0,0],),
    11,
  ),
]