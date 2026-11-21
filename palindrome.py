text = input("Enter a string: ").strip()

if text == text[::-1]:
    print(text, "is a Palindrome")
else:
    print(text, "is not a Palindrome")