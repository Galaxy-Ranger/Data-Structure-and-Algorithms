n = int(input("Enter any Number: "))
temp = n

def divide_evenly(temp):
  count = 0
  while temp > 0:
    rem = temp % 10
    if rem != 0 and n % rem == 0:
      count += 1
    temp = temp // 10
  return count

print(f"{n} is divisible by {divide_evenly(temp)} digits only.")