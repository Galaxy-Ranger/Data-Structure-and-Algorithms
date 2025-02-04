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
#* 1
#* 2 2
#* 3 3 3
#* 4 4 4 4
#* 5 5 5 5 5

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
print()

# Pattern - 8
# *********
#  *******
#   *****
#    ***
#     *

def pattern8(n):
  for i in range(n, 0 , -1):
    # spaces
    for space in range(n - i):
      print(end="  ")
    # stars
    for star in range(1, 2 * i):
      print("*", end=" ")
    print()
pattern8(n)
print()

# Pattern - 9
#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *

def pattern9(n):
  pattern7(n)
  for i in range(n-1, 0, -1):
    # spaces
    for space in range(n - i):
      print(end="  ")
    # stars
    for star in range(1, 2 * i):
      print("*", end=" ")
    print()
pattern9(n)
print()

# Pattern - 10
# *
# **
# ***
# **
# *

def pattern10(n):
  for i in range(n):
    for j in range(i + 1):
      print("*", end=" ")
    print()
  for i in range(n-1, 0, -1):
    for j in range(i):
      print("*", end=" ")
    print()
pattern10(n)
print()

# Pattern - 11
#* 1
#* 0 1
#* 1 0 1
#* 0 1 0 1
#* 1 0 1 0 1

def pattern11(n):
  for i in range(1, n + 1):
    for j in range(1, i + 1):
      if((i + j) % 2 == 0):
        print(1, end=" ")
      else:
        print(0, end=" ")
    print()
pattern11(n)
print()

# Pattern - 12
#* 1      1
#* 12    21
#* 123  321
#* 12344321

def pattern12(n):
  for i in range(1, n + 1):
    # digits
    for d in range(1, i + 1):
      print(d, end=" ")
    # spaces
    for space in range(n - i):
      print(end="  ")
    # spaces
    for space in range(n - i):
      print(end="  ")
    # digits in reverse order
    for rev_d in range(i, 0, -1):
      print(rev_d, end=" ")
    print()
pattern12(n)
print()

# Pattern - 13
#* 1
#* 2 3
#* 4 5 6
#* 7 8 9 10

def pattern13(n):
  counter = 1
  for i in range(n):
    for j in range(i + 1):
      print(counter, end=" ")
      counter += 1
    print()
pattern13(n)
print()

# Pattern - 14
#* A
#* A B
#* A B C
#* A B C D
#* A B C D E

def pattern14(n):
  for i in range(n):
    char = 'A'
    for j in range(i + 1):
      print(char, end=" ")
      char = chr(ord(char) + 1)  # built-in ord() function used to convert char to int and chr is used to convert int to char
    print()
pattern14(n)
print()

# Pattern - 15
#* A B C D E
#* A B C D
#* A B C
#* A B
#* A

def pattern15(n):
  for i in range(n, 0, -1):
    char = 'A'
    for j in range(1, i + 1):
      print(char, end=" ")
      char = chr(ord(char) + 1)
    print()
pattern15(n)
print()

# Pattern - 16
#* A
#* B B
#* C C C
#* D D D D
#* E E E E E

def pattern16(n):
  char = 'A'
  for i in range(1, n + 1):
    for j in range(1, i + 1):
      print(char, end=" ")
    char = chr(ord(char) + 1)
    print()
pattern16(n)
print()

# Pattern - 17
#*      A
#*    A B A
#*  A B C B A
#* A B C D C B A

def pattern17(n):
  for i in range(1, n + 1):
    char = 'A'
    # spaces
    for space in range(n - i):
      print(end="  ")
    # characters (sequentially)
    for j in range(1, i + 1):
      print(char, end=" ")
      char = chr(ord(char) + 1)
    # characters (reversely)
    j = i - 1
    c = 'A'
    c = chr(ord(c) + j-1)
    while i > 1 and j > 0:
      print(c, end=" ")
      c = chr(ord(c) - 1)
      j -= 1
    print()
pattern17(n)
print()

# Pattern - 18
#* E
#* D E
#* C D E
#* B C D E
#* A B C D E

def pattern18(n):
  char = chr(ord('A') + n - 1)
  for i in range(1, n + 1):
    for j in range(1, i + 1):
      print(char, end=' ')
      char = chr(ord(char) + 1)
    char = chr(ord(char) - (i + 1))
    print()
pattern18(n)
print()

# Pattern - 19
#* E
#* E D
#* E D C
#* E D C B
#* E D C B A

def pattern19(n):
  for i in range(1, n + 1):
    char = chr(ord('A') + n - 1)
    for j in range(1, i + 1):
      print(char, end=' ')
      char = chr(ord(char) - 1)
    print()
pattern19(n)
print()

# Pattern - 20
# **********
# ****  ****
# ***    ***
# **      **
# *        *
# *        *
# **      **
# ***    ***
# ****  ****
# **********

def pattern20(n):
  # top half of diamond
  x = 2 * n
  for i in range(x, 0, -2):
    # stars
    for star in range(1, i // 2 + 1):
      print("*", end=" ")
    # spaces
    for space in range(x - (2 * (i // 2))):
      print(end="  ")
    # stars
    for star in range(1, i // 2 + 1):
      print("*", end=" ")
    print()
  # bottom half of diamond
  for i in range(2, x + 1, 2):
    # stars
    for star in range(i // 2):
      print("*", end=" ")
    # space
    for space in range(x - i):
      print(end="  ")
    # stars
    for star in range(i // 2):
      print("*", end=" ")
    print()
pattern20(n)
print()

# Pattern - 21
# *         *
# * *     * *
# * * * * * *
# * *     * *
# *         *

def pattern21(n):
  # top half of butterfly
  for i in range(1, n + 1):
    # stars
    for star in range(1, i + 1):
      print("*", end=" ")
    # spaces
    for space in range(2 * (n - i)):
      print(end="  ")
    # stars
    for star in range(i, 0, -1):
      print("*", end=" ")
    print()
  # bottom half of butterfly
  for i in range(n-1, 0, -1):
    # start
    for star in range(1, i + 1):
      print("*", end=" ")
    # spaces
    for space in range(2 * (n - i)):
      print(end="  ")
    # stars
    for star in range(i, 0, -1):
      print("*", end=" ")
    print()
pattern21(n)
print()

# Pattern - 22
# *****
# *   *
# *   *
# *   *
# *****

def pattern22(n):
  for i in range(1, n + 1):
    for j in range(1, n + 1):
      if(i == 1 or j == 1 or i == n or j == n):
        print("*", end="")
      else:
        print(end=" ")
    print()
pattern22(n)
print()