from functools import reduce

def process_list_sum(lst):
    filtered = list(filter(lambda x: x % 2 == 0, lst))
    mapped = list(map(lambda x: x ** 2, filtered))
    total = reduce(lambda x, y: x + y, mapped)
    return filtered, mapped, total

def main():
    nums = list(map(int, input("Enter numbers separated by space: ").split()))
    filtered, mapped, total = process_list_sum(nums)
    print("Filtered:", filtered)
    print("Mapped (Squares):", mapped)
    print("Sum:", total)

if __name__ == "__main__":
    main()
