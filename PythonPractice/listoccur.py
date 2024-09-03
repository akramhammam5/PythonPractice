def array_front9(nums):
  for i in range(len(nums)):
    if nums[i] == 9 and nums.index(9) <4:
      return True
  return False

