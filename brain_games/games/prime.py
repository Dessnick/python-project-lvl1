def is_prime(number):
    result = simple_int(number)
    if result is not None:
        return result
    result = even_int(number)
    if result is not None:
        return result
    result = above_25(number)
    if result is not None:
        return result
    return 'yes'


def simple_int(number):
    if number == 1:
        return 'no'
    elif number == 2 or number == 3:
        return 'yes'


def even_int(number):
    if (number % 2 == 0 or number % 3 == 0):
        return 'no'


def above_25(number):
    i = 5
    while(i * i <= number):
        if (number % i == 0 or number % (i + 2) == 0):
            return 'no'
        i = i + 6
