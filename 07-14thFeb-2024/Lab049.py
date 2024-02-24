# Functions
# Block of code - which can executed.
# They can return something
# The can't return -> non-return

# They have parameters
# they don't have parameters/ arguments

# Define -> call

def say_hello():  # No return type and no arguments
    print("Hello")


say_hello()


def say_hello_arg(name):  # no return type with argument
    # writing the code
    print("hello", name)


say_hello_arg("Prachitosh")


def say_hello_arg(name, age):  # no return type with argument
    # writing the code
    print("hello", name, age)


say_hello_arg("Prachitosh", 67)
say_hello_arg(123, True)


def say_hello_arg_default(name="Prachitosh"):  # No Return type and argument
    # write the Code
    print("Hello", name)


say_hello_arg_default()
say_hello_arg_default("Linkon")


def sum_number_argument_ret(a, b):
    return a + b


result = sum_number_argument_ret(3, 4)
result2 = sum_number_argument_ret("Prachitosh", "Nayak")
result3= sum_number_argument_ret(10,90)
print(result)
print(result2)
print(result3)
