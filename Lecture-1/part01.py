# Ask Name

print ("What's your name 01?")
name = input("Name: ")
print("Hello " + name)
print("Hello " , name , sep="??")


# Formatting Way

print ("What's your name 02?")
name = input("Name: ")
print(f"Hello " , {name})


# String Functionality

print ("What's your name 03?")
name = input("Name: ")

name = name.strip() # Removing Whitespace from String
name = name.capitalize() #To capitalize the first later
name = name.title() # To Capitalize all first later of the word of a sentence
first, last = name.split(" ") #Split into two parts

print(f"Hello " , {first})


# String Functionality
# (More Efficient Way)

print ("What's your name 04?")

name = input("Name: ").strip().title()

print(f"Hello " , {name})


