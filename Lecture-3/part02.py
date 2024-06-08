def main() :
    num = get_number()
    meow(num)

def get_number():
    while True:
        n = int(input("Value: "))
        if n>0:
            break
    return n

def meow(n):
    for _ in range(n):
        print("Meow")

main()