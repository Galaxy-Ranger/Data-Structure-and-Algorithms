L = [74, 32, 89, 55, 21, 64]

print("Before Insertion Sort: ", L)

#? Approach:

#* Select an element in each iteration from the unsorted array(using a loop).
#* Place it in its corresponding position in the sorted part and shift the remaining elements accordingly (using an inner loop and swapping).
#* The “inner while loop” basically shifts the elements using swapping.

for i in range(1, len(L)):
    j = i
    while j > 0 and L[j] < L[j - 1]:
        L[j], L[j - 1] = L[j - 1], L[j]
        j -= 1

print("After Insertion Sort: ", L)

#* Time Complexity
#? Worst case ---> O(n^2)
#? Best case ---> O(n)
#? Average case ---> O(n^2)