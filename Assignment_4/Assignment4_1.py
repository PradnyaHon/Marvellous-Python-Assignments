def power_of_two(x):
    return (lambda x: x ** 2)(x)

def main():
    num = int(input("Enter a number: "))
    print("Output:", power_of_two(num))

if __name__ == "__main__":
    main()
