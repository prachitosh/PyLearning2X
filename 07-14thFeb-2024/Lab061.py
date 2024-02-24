# Reverse a string
name = input("Enter a name")  # naman
reverse = ""
for i in range(len(name) - 1, -1,-1):  # Add "-1" as the third argument to iterate backward
    reverse = reverse + name[i]

print(reverse)
