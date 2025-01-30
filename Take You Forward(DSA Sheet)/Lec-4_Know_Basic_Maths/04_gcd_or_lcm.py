a = int(input("Enter a value of A: "))
b = int(input("Enter a value of b: "))

# lcm can be found just by using this formula: | a * b | / GCD(a, b)
# and gcd can be found by using this eculidean alogrithm

def lcmAndGcd(a, b):
  def gcd(a, b):
    a, b = min(a, b), max(a, b)
    if a == 0:
      return b
    return gcd(a, b % a)
  def lcm(a, b):
    return abs(a * b) // gcd(a, b)
  return [lcm(a, b), gcd(a, b)]
print(lcmAndGcd(a, b))