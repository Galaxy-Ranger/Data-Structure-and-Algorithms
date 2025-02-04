L = [74, 32, 89, 55, 21, 64]

print("Before Insertion Sort: ", L)

for i in range(1, len(L)):
    j = i
    while j > 0 and L[j] < L[j - 1]:
        L[j], L[j - 1] = L[j - 1], L[j]
        j -= 1

print("After Insertion Sort: ", L)