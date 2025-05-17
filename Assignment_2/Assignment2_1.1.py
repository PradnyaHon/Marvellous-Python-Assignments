from Assignment2_1 import Add, Sub, Mult, Div

def main():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print("Addition:", Add(a, b))
    print("Subtraction:", Sub(a, b))
    print("Multiplication:", Mult(a, b))
    print("Division:", Div(a, b))

if __name__ == "__main__":
    main()
