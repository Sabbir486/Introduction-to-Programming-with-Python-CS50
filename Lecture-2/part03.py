# match (Latest Update)

name = input("Enter your first name: ")

match name:
    case "Harry":
        print("Gryffendoor")

    case "Harmione":
        print("Gryffendoor")

    case "Ron":
        print("Gryffendoor")

    case "Draco":
        print("Slytherin")

    case _:  # For reminding all other Cases
        print("I don't know who you are!")


# Better Way: 


name = input("Enter your second name: ")

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffendoor")

    case "Draco":
        print("Slytherin")

    case _:  # For reminding all other Cases
        print("I don't know who you are!")