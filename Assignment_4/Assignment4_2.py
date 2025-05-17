def multiply(x, y):
    return (lambda a, b: a * b)(x, y)

def main():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Output:", multiply(a, b))

if __name__ == "__main__":
    main()
