class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
      if not s:
        return 0

      n = len(s)
      max_length = 1

      left_i = 0
      right_i = 0
      c_to_index = {}

      while right_i < n:
        right_c = s[right_i]
        if right_c in c_to_index:
          left_i = max(left_i, c_to_index[right_c] + 1)

        c_to_index[right_c] = right_i
        max_length = max(max_length, right_i - left_i + 1)
        right_i += 1

      return max_length

# # Not efficient
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#       if not s:
#         return 0

#       n = len(s)
#       max_length = 1
#       left_i = 0
#       right_i = 1
#       seen = set(s[left_i])

#       while right_i < n:
#         if left_i == right_i:
#           right_i += 1
#           seen.add(s[left_i])
#           continue

#         c = s[right_i]
#         if c in seen:
#           seen.remove(s[left_i])
#           left_i += 1
#         else:
#           max_length = max(max_length, right_i - left_i + 1)
#           seen.add(c)
#           right_i += 1

#       return max_length

tests = [
  (
    ("abcabcbb",),
    3,
  ),
  (
    ("bbbbb",),
    1,
  ),
  (
    ("pwwkew",),
    3,
  ),
  (
    ("wwpflowedddd",),
    7,
  ),
  (
    ("",),
    0,
  ),
  (
    ("b",),
    1,
  ),
]