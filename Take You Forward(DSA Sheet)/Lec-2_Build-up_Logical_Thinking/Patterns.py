# Pattern - 1
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *

n = int(input("Enter Number for Pattern: "))

def pattern1(n):
  for i in range(n):
    for j in range(n):
      print("*", end=" ")
    print()
pattern1(n)
print()

# Pattern - 2
# *
# * *
# * * *
# * * * *
# * * * * *

def pattern2(n):
  for i in range(n):
    for j in range(i + 1):
      print("*", end=" ")
    print()
pattern2(n)
print()

# Pattern - 3
#* 1
#* 1 2
#* 1 2 3
#* 1 2 3 4
#* 1 2 3 4 5

def pattern3(n):
  for i in range(1, n + 1):
    for j in range(1, i + 1):
      print(j, end=" ")
    print()
pattern3(n)
print()

# Pattern - 4
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

def pattern4(n):
  for i in range(n):
    for j in range(i + 1):
      print(i + 1, end=" ")
    print()
pattern4(n)
print()

# Pattern - 5
# * * * * *
# * * * *
# * * *
# * *
# *

def pattern5(n):
  for i in range(n, 0, -1):
    for j in range(i):
      print("*", end=" ")
    print()
pattern5(n)
print()

# Pattern - 6
#* 1 2 3 4 5
#* 1 2 3 4
#* 1 2 3
#* 1 2
#* 1

def pattern6(n):
  for i in range(n, 0, -1):
    for j in range(1, i + 1):
      print(j, end=" ")
    print()
pattern6(n)
print()

# Pattern - 7
#     *
#    ***
#   *****
#  *******
# *********

def pattern7(n):
  for i in range(1, n + 1):
    # spaces
    for space in range(n - i, 0, -1):
      print(end="  ")   # double spaces isliye diya hai jisse ki stars ke beech me spaces de sake nhi to single spaces bhi ho jayega
    # stars
    for star in range(1, 2 * i):
      print("*", end=" ")
    print()
pattern7(n)