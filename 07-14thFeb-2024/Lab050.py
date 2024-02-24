# *args and **Kargs

def f1(a=1, b=1, c=1):
    return a + b + c


f1()
f1(1)
f1(1, 2)
f1(1, 2, 3)
r = f1(c=1, b=22)
print(r)


def print_argument(*args):
    for i in args:
        print(i, end=" ")


print_argument(1)
print_argument(1, 2)
print_argument(1, 2, 3)
print_argument(1, 2, 3, 4)
