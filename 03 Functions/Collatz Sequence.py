def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    else:
        print(3 * number + 1)
        return 3 * number + 1
try:
    input = int(input())
except ValueError:
    print('Type an integer')
while input != 1:
    input = collatz(input)