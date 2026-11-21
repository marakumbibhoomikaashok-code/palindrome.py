
# Program to check Palindrome

text = input("Enter a string: ")

if text == text[::-1]:
    print(text, "is a Palindrome")
else:
    print(text, "is not a Palindrome")
