from functools import reduce

def process_list_product(lst):
    filtered = list(filter(lambda x: 70 <= x <= 90, lst))
    mapped = list(map(lambda x: x + 10, filtered))
    product = reduce(lambda x, y: x * y, mapped)
    return filtered, mapped, product

def main():
    nums = list(map(int, input("Enter numbers separated by space: ").split()))
    filtered, mapped, product = process_list_product(nums)
    print("Filtered:", filtered)
    print("Mapped:", mapped)
    print("Product:", product)

if __name__ == "__main__":
    main()
