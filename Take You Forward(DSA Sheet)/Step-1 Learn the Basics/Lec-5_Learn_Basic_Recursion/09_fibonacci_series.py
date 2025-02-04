n = int(input("Enter any number: "))

def fibo_series(n):
  if n == 0:
    return 0
  if n == 1:
    return 1
  return fibo_series(n - 2) + fibo_series(n - 1)
print(fibo_series(n))