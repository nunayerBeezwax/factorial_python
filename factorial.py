numbers = []

def factorial(number):
    while number >= 1:
        numbers.append(number)
        number-=1

    factorial = 1
    for number in numbers:
        factorial *= number

    return factorial

while True:
    integer = input('Enter a number to see its factorial value: ')
    print factorial(integer)
    
