def singleNumber(nums):
  n = nums
  n.sort()
  xor = n[0]
  for i in range(1, len(nums)):
    xor = xor ^ n[i]
  return xor

nums = [4, 1, 2, 1, 2]
print(f"Single number in the given {nums} list is: {singleNumber(nums)}")