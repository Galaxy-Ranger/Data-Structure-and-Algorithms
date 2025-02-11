def move_zeroes(nums):
  # this loop finds the first zero element in the array and point by i variable
  i = -1
  for j in range(len(nums)):
    if nums[j] == 0:
        i = j
        break
  if i != -1:
    for j in range(len(nums)):
      if i != j and nums[j] != 0 and i < j:
        nums[i], nums[j] = nums[j], nums[i]
        i += 1
  return nums
# print(move_zeroes([0, 1, 0, 3, 12]))
print(move_zeroes([1, 2, 3, 0, 0, 12, 15, 0]))