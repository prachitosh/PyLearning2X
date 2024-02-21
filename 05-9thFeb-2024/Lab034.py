# WAP that calculates and displays the letter grade for a
# given numerical score (e.g.,A,B,C, D or F)
# based on the following grade scale:
# input-score - 89
# output- B
# A: 90-100
# B: 80-89
# C: 70-79
# D: 60-69
# F: 0-59
# If, elif.else

scale = int(input("Enter your num"))

# step 2 and # step 3
# print the output
# logic
# print A -> if scale <=100 and scale >= 90

if 90 <= scale <= 100:
    print("A")
elif 80 <= scale <= 89:
    print("B")
elif scale >= 70 and scale <= 79:
    print("C")
elif scale >= 60 and scale <= 69:
    print("D")
elif scale >=0 and scale <= 59:
    print("F")
else:
    print("Invalid input")
