def find_intersection(l1, l2):
  i = 0
  j = 0
  intersect_list = []
  while i < len(l1) and j < len(l2):
    if l1[i] == l2[j]:
      #! this is very important condition to handle when the first element is intersection element.
      if len(intersect_list) == 0 or intersect_list[-1] != l1[i]:
        intersect_list.append(l1[i])
      i += 1
      j += 1
    elif l1[i] < l2[j]:
      i += 1
    else:
      j += 1
  return intersect_list
  # return list(set(l1) & set(l2))  #! we don't use these inbuilt functions but for knowledge purpose u can remember this syntax
print("Intersection set: {}".format(find_intersection([1,2,2,3,4], [2,2,4,6,7,8])))