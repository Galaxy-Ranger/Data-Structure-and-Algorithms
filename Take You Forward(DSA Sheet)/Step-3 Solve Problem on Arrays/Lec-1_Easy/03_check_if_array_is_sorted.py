# Check if Array Is Sorted
#? You have been given an array ‘a’ of ‘n’ non-negative integers.You have to check whether the given array is sorted in the non-decreasing order or not.

#! Your task is to return 1 if the given array is sorted. Else, return 0.

#* Brute Force Approach ---> O(n^2)
def is_sorted_array(arr):
  n = len(arr)
  for i in range(n):
    for j in range(i+1, n):
      if arr[i] > arr[j]:
        return False
  return True
print(f"Sorted and Rotated array {is_sorted_array([3, 0, 5, 1, 2])}")

#* Optimal Approach ---> O(n)
def is_sorted_array(arr):
  start = 0
  end = len(arr) - 1
  while(start < end):
    if arr[start] > arr[end]:
      return False
    start += 1
    end -= 1
  return True
print(f"Sorted and Rotated array {is_sorted_array([3, 0, 5, 1, 2])}")