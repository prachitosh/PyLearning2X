# continue
# for i in range(1, 10):
#    if i > 1:
#       print(i)

'''for i in range(1, 10):
    if i % 2 == 0:
        print(f"found Even number {i}")
    else:
        print(f"found odd number {i}")'''
for i in range(1, 10):
    if i % 2 == 0:
        print(f"found Even number {i}")
        continue
    print(f"found odd number {i}")

