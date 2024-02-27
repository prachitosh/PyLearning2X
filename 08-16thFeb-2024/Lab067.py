# Tuple collection of the items
# List - collection of items
# Mutable
my_list = [1,2,3,4,5]
my_list[0] = 21
print(my_list)

# Tuple
my_tuple = (1,2,3,4,5)
#my_tuple[1] =21 # Type error: Tuple
print(my_tuple)
print(type(my_tuple))
print(len(my_tuple))

new_tuple = tuple(my_list)
print(new_tuple)