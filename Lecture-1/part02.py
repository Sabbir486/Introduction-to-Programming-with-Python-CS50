# integer (Calculator)

x = int (input("Value 1: "))
y = int (input("Value 2: "))

print(x + y)

# z = int(x) + int(y)
z = (x + y)
print(z)


# float (Calculator)

x1 = float (input("Value 1: "))
y1 = float (input("Value 2: "))

print(x1 + y1)

# z = int(x) + int(y)
z = round(x1 + y1)

print(f"{z:,}") #For giving comma before 3 digits(US System) #Format String


# Division (Calculator)

x2 = float (input("Value 1: "))
y2 = float (input("Value 2: "))

z = round (x2 / y2, 2)

print(z)

