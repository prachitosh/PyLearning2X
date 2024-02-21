# Break

# for -> 1 to 10 -> range(1,11,1), range (1,11)
# i = 5 -> break from the loop -> kick out from the loop

for counter in range(0, 11):
    if counter == 5:
        break
    print(counter)
print("out side of the loop")
