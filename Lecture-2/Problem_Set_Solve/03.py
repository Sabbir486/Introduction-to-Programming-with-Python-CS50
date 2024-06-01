x = input("Greeting: ")

if x.strip().lower().startswith("hello"):
    print("$0")

elif x.strip().lower().startswith("h"):
    print("$20")

else:
    print("$100")
