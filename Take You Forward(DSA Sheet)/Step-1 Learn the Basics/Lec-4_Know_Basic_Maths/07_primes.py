def isPrime(n):
  # code here
  if n <= 1:
    return False
  i = 2
  while i * i <= n:
    if n % i == 0:
      return False
    i += 1
  return True
n = int(input("Enter any number: "))
print(f"Number is prime: {isPrime(n)}")