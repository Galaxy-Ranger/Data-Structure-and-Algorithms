n = int(input("Enter any number: "))
sum = 0
def recursive_sum(n, sum):
  if n == 0:
    return sum
  return recursive_sum(n-1, sum + n)
print(recursive_sum(n, sum))

# Sum of series 1cube + 2cube + 3cube + 4cube ....etc
sum = 0
def recursive_sum(n, sum):
  if n == 0:
    return sum
  return recursive_sum(n-1, sum + (n * n * n))
print(recursive_sum(n, sum))