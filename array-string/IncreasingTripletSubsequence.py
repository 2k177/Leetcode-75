class Solution:
  """
  Given an integer array nums, 
  return true if there exists a triple of indices (i, j, k) 
  such that i < j < k and nums[i] < nums[j] < nums[k]. 
  If no such indices exists, return false.
  """
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        i = j = float('inf')
        for n in nums:
            if n <= i:
                i = n
            elif n <= j:
                j = n
            else:
                return True
        return False
