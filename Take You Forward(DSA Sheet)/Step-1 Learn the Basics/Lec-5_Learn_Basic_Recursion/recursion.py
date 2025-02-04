
#! Infinite Recursion
# n = int(input("Enter any number: "))
# i = 1
# def recursivePrint(i, n):
#   print(i, end=" ")
#   recursivePrint(i + 1, n)
# recursivePrint(i, n)

#? Basic usage of recursion
n = int(input("Enter any number: "))
i = 1
def recursivePrint(i, n):
  if i > n:
    return
  print(i, end=" ")
  recursivePrint(i + 1, n)
recursivePrint(i, n)