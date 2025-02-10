# Given an array arr[]. The task is to find the largest element and return it.

#* Brute Force Approach ---> O(n log(n))
def largest_element(arr):
  arr.sort()
  return arr[-1]
print(f"Largest Element in the array is: {largest_element([1, 8, 7, 56, 90])}")

#* Optimal Approach ---> O(n)
def largest_element(arr):
  # Initialize largest as the first element of the array
  largest = arr[0]

  # Traverse through the array starting from the second element
  for i in range(1, len(arr)):
    # If the current element is greater than largest, update largest
    if arr[i] > largest:
      largest = arr[i]

  # Return the largest element
  return largest
print(f"Largest Element in the array is: {largest_element([1, 8, 7, 56, 90])}")