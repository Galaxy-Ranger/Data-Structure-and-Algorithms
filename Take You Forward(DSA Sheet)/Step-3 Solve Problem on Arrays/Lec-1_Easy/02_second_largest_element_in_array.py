# Find Second Smallest and Second Largest element in the array

#? Given an array of positive integers arr[], return the second largest element from the array. If the second largest element doesn't exist then return -1.

#! Note: The second largest element should not be equal to the largest element.

#* Brute Force Approach ---> O(n log(n))
def second_largest(arr):
  secondLargeElem = float('-inf')  # Initialize with smallest possible integer value
  arr.sort()
  for i in arr:
    if i > secondLargeElem and i < arr[-1]:
      secondLargeElem = i
  return secondLargeElem if secondLargeElem != float('inf') else -1
print(f"Second largest element in array is: {second_largest([12, 35, 1, 10, 35, 1])}")

#* Better Approach ---> O(n)
def second_largest(arr):
  largeElem = secondLargeElem = float('-inf')  # Initialize with smallest possible integer value
  for i in arr:
    if i > largeElem:
      largeElem = i
  for i in arr:
    if i > secondLargeElem and i < largeElem:
      secondLargeElem = i
  return secondLargeElem if secondLargeElem != float('-inf') else -1
print(f"Second largest element in array is: {second_largest([12, 35, 1, 10, 35, 1])}")

#* Optimal Approach with Two Pointers ---> O(n)
def second_largest(arr):
  largeElem = arr[0]
  secondLargeElem = float('-inf')  # Initialize with smallest possible integer value
  for i in range(1, len(arr)):
    if arr[i] > largeElem:
      secondLargeElem, largeElem = largeElem, arr[i]
    elif arr[i] > secondLargeElem and arr[i] < largeElem:
      secondLargeElem = arr[i]
  return secondLargeElem if secondLargeElem != float('-inf') else -1
print(f"Second largest element in array is: {second_largest([12, 35, 1, 10, 34, 1])}")