n = [3, 1, 2, 4, 1, 5, 2, 6, 4]

#! Approach:
#? We will be creating 2 functions mergeSort() and merge().

#! mergeSort(arr[], low, high):
  #? In order to implement merge sort we need to first divide the given array into two halves. Now, if we carefully observe, we need not divide the array and create a separate array, but we will divide the array's range into halves every time. For example, the given range of the array is 0 to 4(0-based indexing). Now on the first go, we will divide the range into half like (0+4)/2 = 2. So, the range of the left half will be 0 to 2 and for the right half, the range will be 3 to 4. Similarly, if the given range is low to high, the range for the two halves will be low to mid and mid+1 to high, where mid = (low+high)/2. This process will continue until the range size becomes.

  #? So, in mergeSort(), we will divide the array around the middle index(rather than creating a separate array) by making the recursive call :
    #* 1. mergeSort(arr,low,mid)   [Left half of the array]
    #* 2. mergeSort(arr,mid+1,high)  [Right half of the array]
    #* where low = leftmost index of the array, high = rightmost index of the array, and mid = middle index of the array.

  #? Now, in order to complete the recursive function, we need to write the base case as well. We know from step 2.1, that our recursion ends when the array has only 1 element left. So, the leftmost index, low, and the rightmost index high become the same as they are pointing to a single element. Base Case: if(low >= high) return;

#! merge(arr[], low, mid, high):
  #? In the merge function, we will use a temp array to store the elements of the two sorted arrays after merging. Here, the range of the left array is low to mid and the range for the right half is mid+1 to high.

  #? Now we will take two pointers left and right, where left starts from low and right starts from mid+1.

  #? Using a while loop( while(left <= mid && right <= high)), we will select two elements, one from each half, and will consider the smallest one among the two. Then, we w?ill insert the smallest element in the temp array.

  #? After that, the left-out elements in both halves will be copied as it is into the temp array.

  #? Now, we will just transfer the elements of the temp array to the range low to high in the original array.

def divide(n, low, high):
  if low >= high:   # Base case
    return [n[low]]   # Return a single element as a list
  mid = (high + low) // 2
  l1 =  divide(n, low, mid)
  l2 = divide(n, mid+1, high)   # mid + 1 to avoid duplication
  return merge(l1, l2)

def merge(l1, l2):
  p1 = 0
  p2 = 0
  l3 = []
  while p1 < len(l1) and p2 < len(l2):
    if l1[p1] <= l2[p2]:
      l3.append(l1[p1])
      p1 += 1
    else:
      l3.append(l2[p2])
      p2 += 1
  while p1 < len(l1):
    l3.append(l1[p1])
    p1 += 1
  while p2 < len(l2):
    l3.append(l2[p2])
    p2 += 1
  return l3

def merge_sort(n):
  print(f"Before Merge Sort: {n}")
  print(f"After Merge Sort:  {divide(n, 0, len(n) - 1)}")   # High should be len(n) - 1
  # print(merge([1, 1, 2, 3, 4], [2, 4, 5, 6]))

merge_sort(n)