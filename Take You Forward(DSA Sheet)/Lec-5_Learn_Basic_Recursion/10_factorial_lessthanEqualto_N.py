n = int(input("Enter any number: "))

#? This is the basic linear fashion to find factorial of number which has O(n) Time complexity
def factorial_number(n):
  if n == 0:
    return 1
  return n * factorial_number(n - 1)
print(factorial_number(n))


# An optimised way when not only we need to find all factorial of number also we need compare with n such that it will be less than or equal to n.
def factorial_lessthan_equalto(f, i, l, n):
  if f > n:
    return l
  l.append(f)
  i += 1
  f *= i
  return factorial_lessthan_equalto(f, i, l, n)
print(factorial_lessthan_equalto(1, 1, [], n))
# Time complexity is O(m) where m is the largest integer such that m! <= n.