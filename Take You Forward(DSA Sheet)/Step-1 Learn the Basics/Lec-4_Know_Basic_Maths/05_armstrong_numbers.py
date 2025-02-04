n = int(input("Enter any number: "))

def armstrongNumber(n):
  l = len(str(n))
  armNum = 0
  t = n
  while n != 0:
    ldigit = n % 10
    armNum += pow(ldigit, l)
    n //= 10
  return armNum == t
print(armstrongNumber(n))