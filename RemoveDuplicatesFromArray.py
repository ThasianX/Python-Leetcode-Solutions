class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 2:
          return len(nums)
        
        lastUniqueIndex = 0
        iterIndex = 1

        while iterIndex < len(nums):
          # If not a duplicate, store the value in the next unique index
          if nums[iterIndex] != nums[lastUniqueIndex]:
            lastUniqueIndex += 1
            nums[lastUniqueIndex] = nums[iterIndex]
          iterIndex += 1
        
        return lastUniqueIndex