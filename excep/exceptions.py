# res = '10' + 5 
# div = 10 / 0

try:
    divisor = int(input('Enter a number but divide in 100 : '))
    result = 100 / divisor
    print(f'The result is {result}')
except ZeroDivisionError as e:
    print('You cannot divide by zero')
    print(e)
except ValueError as e:
    print('You must enter a number')
    print(e)