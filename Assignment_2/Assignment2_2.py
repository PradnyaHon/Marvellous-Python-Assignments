def print_square(n):
    for _ in range(n):
        print("* " * n)

def main():
    num = int(input("Enter a number: "))
    print_square(num)

if __name__ == "__main__":
    main()
