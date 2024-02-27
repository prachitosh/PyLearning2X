# Map

def seq_of_number(num):
    return num ** 2


# result = sq_of_number(10)
# print (result)

numbers = [1,2,3,4,5]

# map()-
# 1. Takes Each item from the list
# 2. execute the function on it.
# 3. Return same number of elements (list)

seq_of_number= list(map(seq_of_number, numbers))
print(seq_of_number)