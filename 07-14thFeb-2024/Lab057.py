# List
# List  - Collection of items (Duplicate is allowed)
my_list = [1, 2, 3, 4]  # (0,1,2)
my_list2 = [1, True, "prachitosh",12.34]

# indexing
print("Element at index 0:", my_list[0])

# changing element
my_list[1] = 20
print("list after changing element at index 1:", my_list)

# append()
my_list.append(5)
print("List after appending:", my_list)

# extend()
my_list.extend([6,7])
print("List after extending:", my_list)

# insert
my_list.insert(1,'a')
print("List after inserting 'a' at index 1:", my_list)

# remove
my_list.remove('a')
print("List after removing 'a':", my_list)


# copy
my_copy_list = my_list.copy()
print(my_copy_list)


#Clear
# my_list.clear()
print("initial list:", my_list)
print(my_copy_list)

print("index of 3 in the list:", my_list.index(3))


# sort
my_copy_list.sort()
print(my_copy_list)
my_copy_list.reverse()
print(my_copy_list)

print(my_copy_list[0])
print(my_copy_list[1])
print(my_copy_list[2])
print(my_copy_list[3])
print(my_copy_list[4])
print(my_copy_list[5])
print(my_copy_list[6])