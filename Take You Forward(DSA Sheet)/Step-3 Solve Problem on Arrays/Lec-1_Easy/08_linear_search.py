
#* Binary Search Implementations ---> O(log(n))
print("Binary Search Implementation")

def searchInSorted(arr, k):
  start = 0
  end = len(arr) - 1
  while start <= end:
    mid = (start + end) // 2
    if arr[mid] == k:
      return True
    elif arr[mid] < k:
      start = mid + 1
    else:
      end = end - 1
  return False

arr = [1, 2, 3, 4, 5, 6]  # The sorted array
k = 6  # The number to search for
ans =  searchInSorted(arr, k)
if ans:
  print(f"{k} is present in the array")
else:
  print(f"{k} is not present in the array")

#* Linear Search Implementation ---> O(n)
print("Linear Search Implementation")

def linearSearch(arr, k):
  for i in range(len(arr)):
    if arr[i] == k:
      return True
  return False

arr = [1, 2, 3, 4, 5, 6]  # The sorted array
k = 6  # The number to search for
ans = linearSearch(arr, k)
if ans:
  print(f"{k} is present in the array")
else:
  print(f"{k} is not present in the array")