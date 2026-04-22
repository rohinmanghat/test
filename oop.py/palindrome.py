a=input("Enter a word:")
low=a.lower()
b=low[::-1]
if low==b:
    print("The word is a palindrome.")
else:
    print("The word is not a palindrome.")