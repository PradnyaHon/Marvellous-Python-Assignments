from functools import reduce

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def process_list_max(lst):
    filtered = list(filter(lambda x: not is_prime(x), lst))
    mapped = list(map(lambda x: x * 2, filtered))
    maximum = reduce(lambda x, y: x if x > y else y, mapped)
    return filtered, mapped, maximum

def main():
    nums = list(map(int, input("Enter numbers separated by space: ").split()))
    filtered, mapped, maximum = process_list_max(nums)
    print("Filtered (non-primes):", filtered)
    print("Mapped (x2):", mapped)
    print("Maximum:", maximum)

if __name__ == "__main__":
    main()
