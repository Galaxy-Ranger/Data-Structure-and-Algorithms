# L = [74, 32, 89, 55, 21, 64]
L = [1, 2, 3, 4, 5]

print("Before Bubble Sort: ", L)

#? The algorithm steps are as follows:

#* First, we will select the range of the unsorted array. For that, we will run a loop(say i) that will signify the last index of the selected range. The loop will run backward from index n-1 to 0(where n = size of the array). The value i = n-1 means the range is from 0 to n-1, and similarly, i = n-2 means the range is from 0 to n-2, and so on.

#* Within the loop, we will run another loop(say j, runs from 0 to i-1 though the range is from 0 to i) to push the maximum element to the last index of the selected range, by repeatedly swapping adjacent elements.

#* Basically, we will swap adjacent elements(if arr[j] > arr[j+1]) until the maximum element of the range reaches the end.

#* Thus, after each iteration, the last part of the array will become sorted. Like: after the first iteration, the array up to the last index will be sorted, and after the second iteration, the array up to the second last index will be sorted, and so on.

#* After (n-1) iteration, the whole array will be sorted.

n = len(L) - 1
flag = True
while n > 0:
  for j in range(n):
    if L[j] > L[j + 1]:
      L[j], L[j + 1] = L[j + 1], L[j]
      flag = False
  if flag:        #! this condition check if everything is in correct order then don't run the outer loop again and again
    break
  n -= 1
print("After Bubble Sort", L)

#* Time Complexity
#? Worst case ---> O(n^2)
#? Best case ---> O(n)
#? Average case ---> O(n^2)