def CheckSign(number):
    if number > 0:
        print("Positive Number")
    elif number < 0:
        print("Negative Number")
    else:
        print("Zero")

def main():
    num = int(input("Enter a number: "))
    CheckSign(num)

if __name__ == "__main__":
    main()
