L = [74, 32, 89, 55, 21, 64]

print(L)

if (len(L) == 1):
    print("Single Element is always sorted.")
else:
    for i in range(len(L)):
        minIdx = i
        for j in range(i+1, len(L)):
            if(L[j] < L[minIdx]):
                minIdx = j
        (L[i], L[minIdx]) = (L[minIdx], L[i])

print(L)