def collatz(number):
    while number != 1:
        if number % 2 == 0:
            number = number // 2
            print(number)
        else:
            number = 3 * number + 1
            print(number)

if __name__ == '__main__':
    try:
        number = int(input())
        collatz(number)
    except ValueError:
        print("Please enter a Integer Number~")

