'''
In this little assignment you are given a string of space separated numbers, 
and have to return the highest and lowest number.
Examples

high_and_low("1 2 3 4 5") # return "5 1"
high_and_low("1 2 -3 4 5") # return "5 -3"
high_and_low("1 9 3 4 -5") # return "9 -5"

Notes

    All numbers are valid Int32, no need to validate them.
    There will always be at least one number in the input string.
    Output string must be two numbers separated by a single space, 
    and highest number is first.
'''

"1 2 3 4 5"
# Hello
# len, max, min, ord

def high_and_low(numbers_str: str) -> str:
    # Дістати числа з рядка
    # max min

    # Задати початкові min/max [1, 2, 3, 4, 5]
    # min/max: 1
    numbers = numbers_str.split()
    min_number = int(numbers[0])
    max_number = int(numbers[0])
    for number in numbers_str.split():
        int_number = int(number)
        if int_number > max_number:
            max_number = int_number
        if int_number < min_number:
            min_number = int_number
    return f'{max_number} {min_number}'

def high_and_low_alternative(numbers_str: str) -> str:
    # Дістати числа з рядка
    # max min

    numbers = numbers_str.split()
    int_numbers = []
    for number in numbers:
        int_numbers.append(int(number))

    max_number = max(int_numbers)
    min_number = min(int_numbers)
    
    return f'{max_number} {min_number}'

# print(ord("a"))
# high_and_low("1 2 3 4 5")
assert high_and_low("1 2 3 4 5") == "5 1"
assert high_and_low("1 2 -3 4 5") == "5 -3"
assert high_and_low("1 9 3 4 -5") == "9 -5"
