def IsDivisibleBy5(no):
    return no % 5 == 0

def main():
    num = int(input("Enter a number: "))
    result = IsDivisibleBy5(num)
    print(result)

if __name__ == "__main__":
    main()
