n = int(input("Enter any number: "))

def factorial_number(n):
  if n == 0:
    return 1
  return n * factorial_number(n - 1)
print(factorial_number(n))


#? Given a number n, the task is to return the list of the factorial numbers smaller than or equal to n.
def factorial_lessthan(n):
  l = []
  for i in range(1, n + 1):
    factI = factorial_number(i)
    if factI <= n:
      l.append(factI)
  print(l)
factorial_lessthan(n)