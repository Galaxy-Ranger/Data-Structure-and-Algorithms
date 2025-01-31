arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Before array: {arr}")
start = 0
end = len(arr) - 1
def revArr(start, end, arr):
  if start >= end:
    return arr
  arr[start], arr[end] = arr[end], arr[start]
  return revArr(start+1, end-1, arr)
print(f"After array: {revArr(start, end, arr)}")