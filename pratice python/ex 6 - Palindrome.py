string = list(input("Type something: "))
reverse = list(reversed(string))

if string == reverse:
    print("Palindrome word")
else:
    print("Not a palindrome word")

# Better resolution

wrd = input("Type something: ")
rvs = wrd[::-1]
if wrd == rvs:
    print("Palindrome word")
else:
    print("Not a palindrome word")
