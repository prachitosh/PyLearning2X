# Reverse a String

'''str = "Prachitosh"
rev_str = " "
for c in str:
    rev_str = c + rev_str

print(rev_str)'''


# reverse string using function
def reverse_string(str):
    rev_str = ""
    for c in str:
        rev_str = c + rev_str
    return rev_str

#name = reverse_string("Linkon")
#print(name)


original_str = input("Enter the string\n")
original_str = original_str.lower().replace(" ", "")
rev_str = reverse_string(original_str)
print(rev_str)
# palindrome - str = rev_str -> p

if original_str == rev_str:
    print("palindrome")
else:
    print("Not a palindrome")