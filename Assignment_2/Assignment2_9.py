def count_digits(n):
    return len(str(n))

def main():
    num = int(input("Enter a number: "))
    print("Output:", count_digits(num))

if __name__ == "__main__":
    main()
