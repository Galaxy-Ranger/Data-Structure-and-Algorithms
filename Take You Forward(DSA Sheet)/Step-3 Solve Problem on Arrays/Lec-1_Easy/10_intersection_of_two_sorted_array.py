def find_intersection(a, b):
  intersect_dict = {}
  for i in a:
    if i in intersect_dict.keys():
      intersect_dict[i] += 1
    else:
      intersect_dict[i] = 1
  for j in b:
    if j in intersect_dict.keys():
      intersect_dict[j] += 1
    else:
      intersect_dict[j] = 1

  intersect_list = []  #! to store the common elements from both sets
  for i in intersect_dict.keys():
    if intersect_dict[i] == 2:
      intersect_list.append(i)
  return intersect_list
  # return list(set(a) & set(b))  #! we don't use these inbuilt functions but for knowledge purpose u can remember this syntax
print("Intersection set: {}".format(find_intersection([1,2,3,4,5], [2,3,6,7])))