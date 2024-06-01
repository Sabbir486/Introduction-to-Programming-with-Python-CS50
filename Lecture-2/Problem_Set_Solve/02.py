def calculate(expression):
    x, y, z = expression.split(" ")

    x = float(x)
    z = float(z)

    if y == "+":
        result = x + z
    elif y == "-":
        result = x - z
    elif y == "*":
        result = x * z
    elif y == "/":
        result = x / z

    return round(result, 1)

def main():
    expression = input("Expression: ")
    result = calculate(expression)
    print(result)

if __name__ == "__main__":
    main()



