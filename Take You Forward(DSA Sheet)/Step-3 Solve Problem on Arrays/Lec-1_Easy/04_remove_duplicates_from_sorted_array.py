# Remove Duplicates from Sorted Array

#? You are given a sorted integer array 'arr' of size 'n'.
#? You need to remove the duplicates from the array such that each element appears only once.
#? Return the length of this new array.

#! Note: Do not allocate extra space for another array. You need to do this by modifying the given input array in place with O(1) extra memory.

#* Brute Force Approach ---> O(n) and Space Complexity ---> O(n)
def removeDuplicates(arr):
  arr_copy = []
  arr_copy.append(arr[0])  # Add the first element to the new array as it is unique by default

  # Iterate through the array and remove duplicates
  idx = 0
  for i in range(1, len(arr)):
      if arr_copy[idx] != arr[i]:
        arr_copy.append(arr[i])
        idx += 1
  # print(arr_copy)
  return len(arr_copy)
print(f"After Removing duplicates {removeDuplicates([1, 2, 2, 2, 3])}")

#* Two Pointer Approach ---> O(n) and Space Complexity ---> O(1)
def removeDuplicates(arr):
  i = 0
  for j in range(1, len(arr)):
    if arr[i] != arr[j]:
      i += 1
      arr[i] = arr[j] # Update the value at index i with the value at index j
  for i in range(i):
    arr.pop(-1)
  return len(arr)
print(f"After Removing duplicates {removeDuplicates([1, 2, 2, 2, 3])}")

#* Using Set and List Conversion ---> O(n) and Space Complexity ---> O(n)