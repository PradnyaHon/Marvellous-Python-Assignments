def print_reverse_triangle(n):
    for i in range(n, 0, -1):
        print("* " * i)

def main():
    num = int(input("Enter a number: "))
    print_reverse_triangle(num)

if __name__ == "__main__":
    main()
