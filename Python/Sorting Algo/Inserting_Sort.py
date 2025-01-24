L = [74, 32, 89, 55, 21, 64]

print(L)

# if (len(L) < 1):
#     print("Single Element is always sorted.")
# else:
#     for i in range(1, len(L)):
#         for j in range(i):
#             if(L[i] < L[j]):
#                 L.insert(j, L[i])
#                 L.pop(i+1)
#                 break

# print(L)

# agar aap insert() & pop() function use nhi karna chahte ho tab....
if (len(L) < 1):
    print("Single Element is always sorted.")
else:
    for i in range(1, len(L)):
        j = i
        while(j > 0 and L[j] < L[j-1]):  # element pick karo fir usse sorted pile ke piche se check karte jao aur swap karte jao
            (L[j], L[j-1]) = (L[j-1], L[j])
            j = j - 1

print(L)
