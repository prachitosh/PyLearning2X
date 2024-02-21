# Match case
numbers = int(input("enter a numbers 1-6\n"))
match numbers: # Break is not needed in match and Case
    case 1:
        print("You have entered 1")
    case 2:
        print("You have entered 2")
    case 3:
        print("you have entered 3")
    case 4:
        print("you have entered 4")
    case 5:
        print("you have entered 5")
    case 6:
        print("you have entered 6")
    case _:
        print("No idea")


