print([1, 2, 3, 4, 5])
def rotateArray(arr):
    n = len(arr)
    temp = arr[0]
    for i in range(n - 1):
        arr[i] = arr[i+1]
    arr[n-1] = temp
    return arr
print(rotateArray([1, 2, 3, 4, 5]))