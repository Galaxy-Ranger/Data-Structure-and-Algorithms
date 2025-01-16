# user-input
num = int(input("Enter a Number: "))
primeList = []  # storing list of primes

# function to calculate prime numbers
def prime_number(num):
    i = 2
    isPrime = True

    while(i < num):
        if(num % i == 0):
            isPrime = False
            break
        i = i + 1

    if isPrime:
        return True

# iterate over prime list and print it on the output screen
def loopOverPrimeNumbers(primeList):
    for i in primeList:
        print(i, end=", ")
    print()
# print(len(primeList))


# when user want list of prime numbers between 1 to num (num is user-input).
for i in range(2, num):
    if(prime_number(i)):
        primeList.append(i)
print(f"All {num} Prime Numbers")
loopOverPrimeNumbers(primeList)


# when user want a prime number on a specific location (Ex. what is the 100th prime number?)
num = int(input("Enter a Number: "))
counter = 0
i = 2
primeList = []
while(counter != num):
    if(prime_number(i)):
        counter = counter + 1
        primeList.append(i)
    i = i + 1
    # if(counter == 100)
print(f"{num}th Prime Number is: {primeList[-1]}")
# print(len(primeList))


# when user want prime number between start position and ending position?
startNum = int(input("Enter Your Start Number: "))
i = startNum
endNum = int(input("Enter Your End Number: "))
primeList = []

while(i <= endNum):
    if(prime_number(i)):
        primeList.append(i)
    i = i + 1
print(f"All Prime Number Between {startNum} and {endNum}")
loopOverPrimeNumbers(primeList)