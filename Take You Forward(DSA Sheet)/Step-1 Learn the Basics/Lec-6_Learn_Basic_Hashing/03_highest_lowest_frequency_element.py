
#! Problem Statement: Given an array of size N. Find the highest and lowest frequency element.
#* Example 1:
#* Input: array[] = {10,5,10,15,10,5};
#* Output: 10 15
#* Explanation: The frequency of 10 is 3, i.e. the highest and the frequency of 15 is 1 i.e. the lowest.

def highestLowestFrequency(arr):
  # Create a dictionary to store the frequency of each element
  frequency = {}
  highestFrequency = float('-inf')
  highestElement = 0
  lowestFrequency = float('inf')
  lowestElement = 0
  for i in arr:
    if i in frequency.keys():
      frequency[i] += 1
    else:
      frequency[i] = 1
    # highestFrequency = max(highestFrequency, frequency[i])
    # lowestFrequency = min(lowestFrequency, frequency[i])
  for i in frequency.keys():
    if highestFrequency < frequency[i]:
      highestElement = i
      highestFrequency = frequency[i]
    if lowestFrequency > frequency[i]:
      lowestElement = i
      lowestFrequency = frequency[i]
  return [highestFrequency, highestElement, lowestFrequency, lowestElement]
arr = [10,5,10,15,10,5]
print(f"The frequency of {highestLowestFrequency(arr)[1]} is {highestLowestFrequency(arr)[0]}, i.e. the highest and the frequency of {highestLowestFrequency(arr)[3]} is {highestLowestFrequency(arr)[2]} i.e. the lowest.")