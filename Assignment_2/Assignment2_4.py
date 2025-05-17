def sum_of_factors(n):
    return sum(i for i in range(1, n) if n % i == 0)

def main():
    num = int(input("Enter a number: "))
    print("Output:", sum_of_factors(num))

if __name__ == "__main__":
    main()
