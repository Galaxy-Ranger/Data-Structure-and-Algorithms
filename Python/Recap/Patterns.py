for i in range(5):
    for j in range(i+1):
        print("*", end=" ")
    print()

print()

for i in range(5):
    for j in range(i):
        print(end="  ")
    for j in range(5-i):
        print("*", end=" ")
    print()

print()

for i in range(5):
    for j in range(5-i):
        print("*", end=" ")
    print()

print()

for i in range(5):
    for j in range(5-i-1):
        print(end="  ")
    for j in range(i+1):
        print("*", end=" ")
    for j in range(i+1-1):
        print("*", end=" ")
    print()
