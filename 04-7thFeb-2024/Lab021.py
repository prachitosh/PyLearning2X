# String concat
str1 = "Hello"
str2 = "World"
str3 = str1 + str2
print(str3)

name = "Prachitosh"
age = 28

# r = (name + age) # TypeError: can only concatenate str (not "int") to
r = name + str(age)
print(r)

g = "hello"
g += "world"
g = g + "world"
print(g)

# Increment and Decrement ++, __
x = 5
x += 1  # 6
x -= 1
print(x)
x = 10
y = x + 1
print(y)
