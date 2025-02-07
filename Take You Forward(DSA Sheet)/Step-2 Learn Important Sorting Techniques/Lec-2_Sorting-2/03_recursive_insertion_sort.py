arr = [13, 46, 24, 52, 20, 9]

print("Before Recursive Insertion Sort: ", arr)

#! The approach will be the following:
#? First, call the recursive function with the given array, the size of the array, and the index of the selected element(let's say i).

#? Inside that recursive function, take the element at index i from the unsorted array.

#? Then, place the element in its corresponding position in the sorted part(using swapping).

#? After that, Shift the remaining elements accordingly.

#? Finally, call the recursion increasing the index(i) by 1.

#? The recursion will continue until the index reaches n(i.e. All the elements are covered). Base Case: if(i == n) return;

def recursive_insertion_sort(arr, start):
  if start == len(arr):
    return
  i = start
  while i > 0 and arr[i - 1] > arr[i]:
    arr[i - 1], arr[i] = arr[i], arr[i - 1]
    i -= 1
  recursive_insertion_sort(arr, start + 1)
recursive_insertion_sort(arr, 1)

print("Before Recursive Insertion Sort: ", arr)