# condition
# age > 18 --> You are allowed to go to the club
# age < 18 --> you are not allowed

age = int(input("enter your age"))
# if condition return True or False
if age > 18:
    print("You are allowed to go to the club")
else:
    print("You are not allowed")

a = 8
# if a = 5: This will not return condition True or False
if a == 5:
    print("Hi")
else:
    print("Bye")

x = 10
y = 10

# x>y
# x<y
# x==y
if x > y:
    print("x is greater than y")
elif x < y:
    print("x is less than y")
else:
    print("x is equally to y")