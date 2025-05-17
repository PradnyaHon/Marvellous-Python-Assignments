def frequency_of_number():
    n = int(input("Enter number of elements: "))
    numbers = [int(input(f"Element {i+1}: ")) for i in range(n)]
    x = int(input("Enter the number to search: "))
    print("Output:", numbers.count(x))

def main():
    frequency_of_number()

if __name__ == "__main__":
    main()
