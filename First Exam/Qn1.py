"""1. Check given string is palindrome or Not?"""

word=input("Your string pls.....   \n")
reverseWord=word[::-1]
print("Your String Input...    ",word)
print("Your String Reversed...    ",reverseWord)
if(word==reverseWord):
    print("Your input is a PALINDROME")
else:
    print("Your input is NOT a PALINDROME")
