# Problem find the max between 3 numbers
x = int(input("Enter 1st num"))
y = int(input("Enter second num"))
z = int(input("Enter your 3rd num"))
if (x>y) and (x>z):
    print("Max is", x)
elif (y>x) and (y>z):
    print("max y is",y)
else:
  print("max is",z)

'''num1 = int(input("Enter num1"))
num2 = int(input("Enter num2"))
num3 = int(input("Enter num3"))
max_num = max(num1, num2, num3)
print(max_num)'''
