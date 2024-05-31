def convert(text1):

    text1 = text1.replace(":)", "🙂")
    text1 = text1.replace(":(", "🙁")
    return text1

def main():
    text = input("Enter text: ")
    converted_text = convert(text)
    print(converted_text)

if __name__ == "__main__":
    main()
