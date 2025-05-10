def DisplayEvenNumbers():
    for i in range(1, 21):
        if i % 2 == 0:
            print(i, end=" ")

def main():
    DisplayEvenNumbers()

if __name__ == "__main__":
    main()
