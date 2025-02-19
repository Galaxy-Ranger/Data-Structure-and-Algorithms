def find_missing(distinct_list):
  l = len(distinct_list)
  distinct_list.sort()
  # print(distinct_list)
  for i in range(l):
    if i != distinct_list[i]:
      return i
  return l

# print(f"Missing Number in this {[3,0,1]} list is: {find_missing([3,0,1])}.")
# print(f"Missing Number in this {[0,1]} list is: {find_missing([0,1])}.")
print(f"Missing Number in this {[9,6,4,2,3,5,7,0,1]} list is: {find_missing([9,6,4,2,3,5,7,0,1])}.")