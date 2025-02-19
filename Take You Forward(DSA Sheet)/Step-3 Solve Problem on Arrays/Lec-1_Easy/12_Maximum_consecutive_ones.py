def findMaxConsecutiveOnes(nums):
  max_consec = 0
  curr_consec = 0
  for i in nums:
      if i == 1:
        curr_consec += 1
      else:
        curr_consec = 0
      if curr_consec > max_consec:
        max_consec = curr_consec
  return max_consec

nums = [1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1]

print(f"Maximum Consecutive Ones in the Given {nums} list is: {findMaxConsecutiveOnes(nums)}")