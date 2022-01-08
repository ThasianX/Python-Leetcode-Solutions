from typing import List

class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
      n = len(arr)

      # indices should be sorted in asc or desc before being passed in
      def generateNextGreaterIndices(indices: List[int]) -> List[int]:
        res = [None] * n
        stack = []

        for i in range(n):
          # If a greater index is reachable for any indices on the
          # stack, store the next greater index in the relevant
          # index on the stack
          # res[some_index] = next_greater_index_for_some_index
          while stack and indices[stack[-1]] < indices[i]:
            res[indices[stack.pop()]] = indices[i]
          stack.append(i)

        return res
      
      sorted_arr = sorted(range(n), key=lambda x: arr[x])
      odd_next = generateNextGreaterIndices(sorted_arr)
  
      sorted_arr.sort(key=lambda x: arr[x], reverse=True)
      even_next = generateNextGreaterIndices(sorted_arr)
  
      # [odd jump valid, even jump valid]
      # 0 = false, 1 = true
      dp = [[0, 0] for i in range(n)]

      # The end is reachable from itself
      dp[-1] = [1, 1]

      for i in range(n - 2, -1, -1):
        # If odd jump is possible, then its value is whether
        # an even jump is possible from its new position
        if odd_next[i] is not None:
          dp[i][0] = dp[odd_next[i]][1]
        # If even jump is possible, then its value is whether
        # an odd jump is possible from its new position
        if even_next[i] is not None:
          dp[i][1] = dp[even_next[i]][0]
      
      return sum([odd_jump_valid for [odd_jump_valid,_] in dp])
          

        
tests = [
  (
    ([10,13,12,14,15],),
    2,
  ),
  (
    ([2,3,1,1,4],),
    3,
  ),
  (
    ([5,1,3,4,2],),
    3
  )
]

# # Brute force
# class Solution:
#     def oddEvenJumps(self, arr: List[int]) -> int:
#       n = len(arr)

#       def getOddJumpIndex(start_i: int) -> int:
#         min_i = -1
#         curr_i = start_i + 1

#         while curr_i < n:
#           if arr[start_i] <= arr[curr_i] and (min_i == -1 or arr[curr_i] < arr[min_i]):
#             min_i = curr_i
#           curr_i += 1
        
#         return min_i

#       def getEvenJumpIndex(start_i: int) -> int:
#         max_i = -1
#         curr_i = start_i + 1

#         while curr_i < n:
#           if arr[start_i] >= arr[curr_i] and (max_i == -1 or arr[curr_i] > arr[max_i]):
#             max_i = curr_i
#           curr_i += 1
        
#         return max_i

#       valid_jumps = 0

#       for i in range(n):
#         j = 1
#         jump_i = i
#         while jump_i != -1 and jump_i != n - 1:
#           if j % 2 == 0:
#             jump_i = getEvenJumpIndex(jump_i)
#           else:
#             jump_i = getOddJumpIndex(jump_i)
#           j += 1
        
#         if jump_i == n - 1:
#           valid_jumps += 1
      
#       return valid_jumps
          

        
# tests = [
#   (
#     ([10,13,12,14,15],),
#     2,
#   ),
#   (
#     ([2,3,1,1,4],),
#     3,
#   ),
#   (
#     ([5,1,3,4,2],),
#     3
#   )
# ]