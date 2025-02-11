print([1, 2, 3, 4, 5])
k = 3
print("Brute Force Approach")
print(f"shifting element to the left by {k} palces")

#* Brute Force Approach ---> O(n^2)
def rotateArray(arr, k):
    n = len(arr)
    for place in range(k):
      temp = arr[0]
      for i in range(n - 1):
          arr[i] = arr[i+1]
      arr[n-1] = temp
    return arr
print(rotateArray([1, 2, 3, 4, 5], k))

print(f"shifting element to the right by {k} palces")
def rotateArray(arr, k):
    n = len(arr)
    for place in range((k % n)):  #? why k % n because at every k rotation when k == n it is same as the original array.
      temp = arr[-1]
      pos = n-1
      while pos > 0:
          arr[pos] = arr[pos - 1]
          pos -= 1
      arr[0] = temp
    return arr
print(rotateArray([1, 2, 3, 4, 5], k))
# print(rotateArray([1, 2, 3, 4, 5, 6, 7], 2))

print("Better Approach")
print(f"shifting element to the left by {k} palces")
#* Better Approach ---> O()
def rotateArray(arr, k):
  temp = arr[ : k]
  n = len(arr)
  # first place the first k element to the left
  for i in range(k, n):
    arr[i - k] = arr[i]
  # then place the temp array to the left
  for i in range(len(temp)):
    arr[n - k + i] = temp[i]
  return arr
print(rotateArray([1, 2, 3, 4, 5], k))

print(f"shifting element to the right by {k} palces")
def rotateArray(arr, k):
  temp = arr[-1 * k:]
  n = len(arr)
  # first place the first n - k element to the right
  for i in range(1, (n - k + 1)):
    arr[n - i] = arr[n - k - i]
  # then place the temp array to the left
  for i in range(len(temp)):
    arr[i] = temp[i]
  return arr
print(rotateArray([1, 2, 3, 4, 5], k))