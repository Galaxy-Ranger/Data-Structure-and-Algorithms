n = int(input("Enter any number: "))
# Print 1 to N
def print_1toN(n):
  if n == 0:
    return
  print_1toN(n-1)
  print(n, end=" ")
print_1toN(n)
print()
# Print N to 1
def print_1toN(n):
  if n == 0:
    return
  print(n, end=" ")
  print_1toN(n-1)
print_1toN(n)