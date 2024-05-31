# Parity : + - * / %

x = int(input("Value: "))

if(x%2==0):
    print("Even")

else:
    print("Odd")


# Other Way: By Creating Function

def main():
    x = int(input("Value: "))

    if is_even(x):
         print("Even")

    else:
        print("Odd")

def is_even(num):
    if (num%2==0):
        return True
    else:
        return False
    
    # ALLIGANT WAY: return num % 2 == 0

main()
