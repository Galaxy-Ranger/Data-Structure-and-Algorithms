n = int(input("Enter any number: "))

def isPalindrome(n):
  l = len(str(n))
  if n < 0:
    return False
  if l == 1:
    return True
  i = 0
  j = l-1
  while(i < j):
    if(str(n)[i] != str(n)[j]):
      return False
    i += 1
    j -= 1
  return True

print(isPalindrome(n))