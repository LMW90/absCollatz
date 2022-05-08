def collatz(number):
    if number == 1:
        return None
    elif number % 2 == 0:
        number = number // 2
        print(number)
        collatz(number)
    else:
        number = number * 3 +1
        print(number)
        collatz(number)


print('Enter a number.')
num = int(input())
collatz(num)