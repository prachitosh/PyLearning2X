# format String
# 2 x 1 =2
num = 2
print(f" {num}x1=  {num}")
print(f" {num}x2=  {num*2}")
print(f"{num}x3=  {num*3}")
print(f"{num}x4=  {num*4}")

# 10 x1 =10

print("Enter your num")
n = int(input())
for i in range(10):
   print(n, "x", i + 1, "=", n * (i + 1))
