x = int(input("Enter any number: "))

ownX = x
MAX_INT = 2**31 - 1
MIN_INT = -2**31
temp = 0
sign = -1 if x < 0 else 1
ownX = abs(ownX)

def reverse_number(ownX, temp):
  while ownX != 0:
    ldigit = ownX % 10
    if temp > MAX_INT // 10:
      return 0
    elif temp < MIN_INT // 10:
      return 0
    else:
      temp = (temp * pow(10,1)) + ldigit
    ownX = ownX // 10
  return temp * sign

print(reverse_number(ownX, temp))