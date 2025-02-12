def find_union(a, b):
  i = 0
  j = 0
  union_list = []

  while i < len(a) and j < len(b):
    if a[i] <= b[j]:
      if len(union_list) == 0 or union_list[-1] != a[i]:
        union_list.append(a[i])
      i += 1
    elif a[i] > b[j]:
      if len(union_list) == 0 or union_list[-1] != b[j]:
        union_list.append(b[j])
      j += 1
  # append remaining elements of a and b to the union_list
  while i < len(a):
    if len(union_list) == 0 or union_list[-1] != a[i]:
      union_list.append(a[i])
    i += 1
  while j < len(b):
    if len(union_list) == 0 or union_list[-1] != b[j]:
      union_list.append(b[j])
    j += 1
  return union_list
  # return list(set(a) | set(b))  #! we don't use these inbuilt functions but for knowledge purpose u can remember this syntax
print("Union set: {}".format(find_union([1,2,3,4,5], [2,3,6,7])))