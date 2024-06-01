x = input("What is the Answer to the Great Question of Life, the Universe, and Everything?" )

match x.strip().lower():

    case "42" | "FoRty TwO" | "forty-two" | "forty two":
        print("Yes")

    case _:
        print("No")
