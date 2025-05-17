def sum_of_digits(n):
    return sum(int(d) for d in str(n))

def main():
    num = int(input("Enter a number: "))
    print("Output:", sum_of_digits(num))

if __name__ == "__main__":
    main()
