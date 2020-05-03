def is_prime(number):
    if number == 1:
        return 'no'
    elif number == 2 or number == 3:
        return 'yes'
    if (number % 2 == 0 or number % 3 == 0):
        return 'no'
    i = 5
    while(i * i <= number):
        if (number % i == 0 or number % (i + 2) == 0):
            return 'no'
        i = i + 6
    return 'yes'
