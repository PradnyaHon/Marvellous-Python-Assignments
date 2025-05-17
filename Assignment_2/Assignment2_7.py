def print_pattern_fixed(n):
    for _ in range(n):
        for j in range(1, n + 1):
            print(j, end=" ")
        print()

def main():
    num = int(input("Enter a number: "))
    print_pattern_fixed(num)

if __name__ == "__main__":
    main()
