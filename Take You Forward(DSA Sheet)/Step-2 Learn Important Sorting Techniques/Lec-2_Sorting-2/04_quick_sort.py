arr = [4, 6, 2, 5, 7, 9, 1, 3]

print("Before Quick Sort: ", arr)

#! The algorithm steps are the following for the quickSort() function:
  #? Initially, the low points to the first index and the high points to the last index(as the range is n i.e. the size of the array).

  #? After that, we will get the index(where the pivot should be placed after sorting) while shifting the smaller elements on the left and the larger ones on the right using a partition() function discussed later.

  #? Now, this index can be called the partition index as it creates a partition between the left and the right unsorted subarrays.

  #? After placing the pivot in the partition index(within the partition() function specified), we need to call the function quickSort() for the left and the right subarray recursively. So, the range of the left subarray will be [low to (partition index - 1)] and the range of the right subarray will be [(partition index + 1) to high].

  #? This is how the recursion will continue until the range becomes 1.

#! Now, let’s understand how to implement the partition() function to get the partition index.
  #? Inside the function, we will first select the pivot(i.e. arr[low] in our case).

  #? Now, we will again take two-pointers i and j. The i pointer points to low and the j points to high.

  #? Now, the pointer i will move forward and find the first element that is greater than the pivot. Similarly, the pointer j will move backward and find the first element that is smaller than the pivot.

  #? Here, we need to add some checks like i <= high-1 and j >= low+1. Because it might happen that i is standing at high and trying to proceed or j is standing at low and trying to exceed.

  #? Once we find such elements i.e. arr[i] > pivot and arr[j] < pivot, and i < j, we will swap arr[i] and arr[j].

  #? We will continue step 3 and step 4, until j becomes smaller than i.

  #? Finally, we will swap the pivot element(i.e. arr[low]) with arr[j] and will return the index j i.e. the partition index.

#* Note: In the function, we have kept the elements equal to the pivot on the left side. If you choose to place them on the right, check 1 will be arr[i] < pivot and check 2 will be arr[j] >= pivot.

def quick_sort(arr, low, high):
  if low < high:
    partition = placing_the_pivot(arr, low, high)
    quick_sort(arr, low, partition - 1)
    quick_sort(arr, partition + 1, high)

def placing_the_pivot(arr, low, high):
  pivot = low
  i = low
  j = high
  while i < j:
    while arr[i] <= arr[pivot] and i <= high - 1:
      i += 1
    while arr[j] > arr[pivot] and j >= low + 1:
      j -= 1
    if i < j:
      arr[i], arr[j] = arr[j], arr[i]
  arr[low], arr[j] = arr[j], arr[low]
  return j
quick_sort(arr, 0, len(arr) - 1)

print("After Quick Sort: ", arr)