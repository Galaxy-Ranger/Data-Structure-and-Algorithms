arr = [2, 3, 2, 3, 5]

# Function to count the frequency of all elements from 1 to N in the array.
def frequencyCount(arr):
  freq = [0] * (len(arr))
  for i in range(len(arr)):
    freq[arr[i]-1] += 1
  return freq
print(frequencyCount(arr))
#* Output: [0, 2, 2, 0, 1]
#* Explanation: We have: 1 occurring 0 times, 2 occurring 2 times, 3 occurring 2 times, 4 occurring 0 times, and 5 occurring 1 time.