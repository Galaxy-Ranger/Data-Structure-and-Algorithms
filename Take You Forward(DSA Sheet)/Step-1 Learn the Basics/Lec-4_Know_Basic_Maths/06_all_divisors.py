from math import sqrt


n = int(input("Enter any number: "))

def all_divisors(n):
  sumOfDivisors = 0
  if n == 0:
    return 0
  if n == 1:
    return 1
  for i in range(2, n + 1):
    t = i
    for j in range(1, int(sqrt(i)) + 1):
      if i == j * j:
        sumOfDivisors += j
      elif i % j == 0:
        sumOfDivisors += j
        sumOfDivisors += t // j
  return sumOfDivisors + 1
print(all_divisors(n))

#* Above code Time complexity is O(n sqrt(n))
def sum_of_all_divisors(n):
  div_sum = [0] * (n + 1)

  for i in range(1, n + 1):  # Har number ke liye
    for j in range(i, n + 1, i):  # Uske multiples ke sum me add karo
      div_sum[j] += i

  return sum(div_sum)  # 1 se n tak ke saare divisors ka sum return karo

n = int(input("Enter any number: "))
print(sum_of_all_divisors(n))

#* and this code time complexity is O(n log(n)) and this algorithm is Divisor Summation Using Sieve.
#! How It Works?
#? 1. Ek array div_sum banao jo har number ka sum of divisors store karega.

    #* Pehle sabko 0 se initialize kar do.
    #* div_sum[i] ka matlab hai number i ka sum of divisors.
#? 2. Har number i ke liye uske multiples update karo

    #? Example: i=2 ke liye
        #* div_sum[2] me +2 add karo
        #* div_sum[4] me +2 add karo
        #* div_sum[6] me +2 add karo
    #? Example: i=3 ke liye
        #* div_sum[3] me +3 add karo
        #* div_sum[6] me +3 add karo
        #* div_sum[9] me +3 add karo
#? 3. Jab loop khatam hoga, to div_sum me har number ka divisor sum store hoga.

#! This approach is pure mathematical equation [NOT IMPORTANT]
def sum_of_all_divisors_(n):
    total_sum = 0
    for i in range(1, n + 1):
        total_sum += i * (n // i)  # i contributes (n // i) times
    return total_sum

n = int(input("Enter any number: "))
print(sum_of_all_divisors_(n))

#* above Algorithm Time Complexity is O(n)

#? 1. Understanding the Formula
    #* The key observation is that a number i appears as a divisor for multiple numbers.
    #* The count of numbers divisible by i from 1 to n is ⌊ n // i ⌋.
    #* This means that i contributes to the sum ⌊ n // i ⌋ times.
#? 2. Summation Calculation
    #* Instead of iterating through each number and finding its divisors separately, we iterate from 1 to n and use the formula:
    #* summation i=1 to n ---> i * [n // i]
    #* Here, i × ⌊ n // i ⌋ directly adds the contribution of i to all its multiples at once.

#? Example Walkthrough for n = 6
    #* i = 1 ⇒ 1 × (6 // 1) = 1 × 6 = 6
    #* i = 2 ⇒ 2 × (6 // 2) = 2 × 3 = 6
    #* i = 3 ⇒ 3 × (6 // 3) = 3 × 2 = 6
    #* i = 4 ⇒ 4 × (6 // 4) = 4 × 1 = 4
    #* i = 5 ⇒ 5 × (6 // 5) = 5 × 1 = 5
    #* i = 6 ⇒ 6 × (6 // 6) = 6 × 1 = 6
    #* f(6) = 6 + 6 + 6 + 4 + 5 + 6 = 33