
#* Naive way to find the repeated element in the array
arr = [1, 2, 3, 2, 4, 4, 1, 0, 5, 6]
for i in range(max(arr) + 1):
  count = 0
  for j in range(len(arr)):
    if i == arr[j]:
      count += 1
  print(f"count {i} = {count}")
print("Time Complexity is: O(Q * N)")
#* Which has time complexity O(Q * N)  where Q is the largest element in the array and N is the number of elements in the array

#? Using Hashing Concept

#* Integer Hashing Array
#! ----------- Taking input from the user ---------
# how many length of array user want
n = int(input("What is the size of an array you want to:  "))
user_arr = []
# taking input from user and storing it in array
for i in range(n):
  user_arr.append(int(input("Enter the elements: ")))
#! ------------------------------------------------

#! ------- Precomputation to find repeated element in the array -------
# creating hash array from the user_arr
hashArr = [0] * (max(user_arr) + 1)    # hashArr initialized with (max element + 1) elements
for i in user_arr:
  hashArr[i] += 1
#! --------------------------------------------------------------------

#! ------- Accessing elements from hash array -------
# how many elements you want to access
n = int(input("Enter the number of elements you want to access: "))

# taking input from user and accessing element from hash array
for i in range(n):
  ele = int(input("Enter the element you want to access: "))
  print(f"Repetation of {ele} in the array: {hashArr[ele]}")
#! ---------------------------------------------------

#* Character Hashing Array
#! ----------- Taking input from the user ---------
user_arr = input("Enter any string: ")
#! ------------------------------------------------

#! ------- Precomputation to find repeated element in the array -------
# creating hash array from the user_arr
hashArr = [0] * (27)    # hashArr initialized with (27) elements
for i in user_arr:
  hashArr[ord(i.upper()) - 65] += 1   # (i - 65) will convert the ascii value of i to indices of the array.
#! --------------------------------------------------------------------

#! ------- Accessing elements from hash array -------
# how many elements you want to access
n = int(input("Enter the number of elements you want to access: "))

# taking input from user and accessing element from hash array
for i in range(n):
  ele = input("Enter the element you want to access: ")
  print(f"Repetation of {ele} in the array: {hashArr[ord(ele.upper()) - 65]}")
#! ---------------------------------------------------

print("Time Complexity when storing element in hash array: O(N)")
print("Time Complexity when accessing element from hash array: O(1)")