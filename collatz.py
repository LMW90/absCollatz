def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return number * 3 +1


print('Enter a number.')
num = int(input())
while True:
    num = collatz(num)
    print(num)
    if num == 1:
        break