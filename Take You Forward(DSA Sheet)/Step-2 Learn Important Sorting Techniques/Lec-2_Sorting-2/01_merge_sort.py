n = [3, 1, 2, 4, 1, 5, 2, 6, 4]

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