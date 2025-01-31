s = input("Enter any string: ")

s = "".join([i for i in s if i.isalnum()]).lower()
print(f"String is palindrome: {s[::-1] == s}")