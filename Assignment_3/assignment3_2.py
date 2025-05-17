def max_of_elements():
    n = int(input("Enter number of elements: "))
    numbers = [int(input(f"Element {i+1}: ")) for i in range(n)]
    print("Output:", max(numbers))

def main():
    max_of_elements()

if __name__ == "__main__":
    main()
