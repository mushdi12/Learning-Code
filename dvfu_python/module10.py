# task A
def print_hello(name):
    print(f'Hello, {name}!')

# task B
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# task C
def number_length(number):
    length = 0 if number != 0 else 1
    while number != 0:
        number = int(number / 10)
        length += 1
    return length

# task D
def month(num, lang):
    MONTHS = {
        'ru': ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль',
               'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь'],
        'en': ['January', 'February', 'March', 'April', 'May', 'June', 'July',
               'August', 'September', 'October', 'November', 'December']
             }

    return MONTHS[lang][num - 1]

# task E
def split_numbers(string):
    return tuple([int(number) for number in string.split()])

# task F
history = set()


def modern_print(string):
    if string not in history:
        print(string)
        history.add(string)

# task G
def can_eat(horse, cell):
    x = abs(horse[0] - cell[0])
    y = abs(horse[1] - cell[1])
    return {x, y} == {1, 2}

# task H
def is_palindrome(test):
    if isinstance(test, int) or isinstance(test, float):
        test = str(abs(test))
    return test == test[::-1]

# task I
def is_prime(number):
    if number < 2:
        return False

    divider = 2
    while divider <= number ** 0.5:
        if number % divider == 0:
            return False
        divider += 1
    return True

# task J
def merge(sequence_1, sequence_2):
    queue_1 = list(sequence_1)
    queue_2 = list(sequence_2)
    sequence = []
    while queue_1 and queue_2:
        if queue_1[0] > queue_2[0]:
            sequence.append(queue_2.pop(0))
        else:
            sequence.append(queue_1.pop(0))
    sequence.extend(queue_1)
    sequence.extend(queue_2)
    return tuple(sequence)

