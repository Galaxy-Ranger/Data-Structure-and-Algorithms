arr = [13, 46, 24, 52, 20, 9]

print("Before Rccursive Bubble Sort: ", arr)

#! The approach will be the following:
#? First, call the recursive function with the given array and the range of n(size of the array).

#? Inside that recursive function, repeatedly swap 2 adjacent elements if arr[j] > arr[j+1].

#? Here, the maximum element of the unsorted array reaches the end of the unsorted array after each recursive call.

#? Each time after step 2, call the recursion again decreasing the range by 1.

#? The recursion will continue until the range(i.e. the size) of the array is reduced to 1. Base Case: if(n == 1) return;

def recursive_bubble_sort(arr, end, flag):
  if end == 1:
    return
  for i in range(end - 1):
    if arr[i] > arr[i + 1]:
      arr[i], arr[i + 1] = arr[i + 1], arr[i]
      flag = False
  if flag:  # optimizing for best case
    return
  recursive_bubble_sort(arr, end - 1, flag)
recursive_bubble_sort(arr, len(arr), True)

print("After Rccursive Bubble Sort: ", arr)