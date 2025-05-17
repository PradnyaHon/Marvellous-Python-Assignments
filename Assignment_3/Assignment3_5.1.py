# main.py
from Assignment3_5 import ChkPrime

def ListPrime():
    n = int(input("Enter number of elements: "))
    numbers = [int(input(f"Element {i+1}: ")) for i in range(n)]
    prime_sum = sum(num for num in numbers if ChkPrime(num))
    print("Output:", prime_sum)

def main():
    ListPrime()

if __name__ == "__main__":
    main()
