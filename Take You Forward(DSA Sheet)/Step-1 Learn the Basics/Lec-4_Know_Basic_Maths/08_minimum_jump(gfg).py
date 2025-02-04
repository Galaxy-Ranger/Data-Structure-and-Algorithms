def minJumps(arr):   # greedy algorithm lagegi..... abhi mai waha tak pahucha nhi hu GPT code...
  n = len(arr)

  if n <= 1:
    return 0  # No jump needed if only one element

  if arr[0] == 0:
    return -1  # If the first element is 0, it's impossible to move forward

  jumps = 0
  current_end = 0
  farthest = 0

  for i in range(n):
    # Update the farthest we can reach from index i
    farthest = max(farthest, i + arr[i])

    # If we've reached the end of the current jump
    if i == current_end:
      jumps += 1
      current_end = farthest

      # If we've reached or surpassed the last index
      if current_end >= n - 1:
        return jumps

    # If we're stuck (i.e., can't move forward), return -1
    if i >= farthest:
      return -1

  return -1  # If we couldn't reach the last index
print(minJumps([1,3,5,8,5,2,6,7,6,0,8]))