n = int(input("Enter any number: "))

def printN_recursive(n):
  if n == 0:
    return
  print("GFG", end=" ")
  printN_recursive(n-1)
printN_recursive(n)