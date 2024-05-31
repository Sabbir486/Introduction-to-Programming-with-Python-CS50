# Conditional Statements:

x = int(input("Value01: "))
y = int(input("Value02: "))

if (x<y):
    print("X is less than Y")

elif (x>y):
    print("X is greater than Y")

else:
    print("X is equal to Y")


# OR Statements:

x = int(input("Value03: "))
y = int(input("Value04: "))

if (x<y or x>y):
    print("X is not equal to Y")

else:
    print("X is equal to Y")


# AND Statements:

s = int(input("score1: "))

if (s>= 90 and s<=100):
    print("Grade: A+")

elif (s>= 80 and s<=89):
    print("Grade: B+")

elif (s>= 70 and s<=79):
    print("Grade: C+")

else:
    print("Grade: F")


# Second Process:

s = int(input("score2: "))

if (s>= 90):
    print("Grade: A+")

elif (s>= 80):
    print("Grade: B+")

elif (s>= 70):
    print("Grade: C+")

else:
    print("Grade: F")



