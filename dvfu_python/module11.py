# task A
def make_list(length, value=0):
    lst = []
    for _ in range(length):
        lst.append(value)
    return lst

# task B
def make_matrix(size, value=0):
    if isinstance(size, int):
        size = [size, size]
    result = [[value] * size[0] for _ in range(size[1])]
    return result

# task C
def gcd(*numbers):
    a, *tail = numbers
    for b in tail:
        while b:
            a, b = b, a % b
    return a

# task D
def month(num, lang='ru'):
    MONTHS = {
        'ru': ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль',
               'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь'],
        'en': ['January', 'February', 'March', 'April', 'May', 'June', 'July',
               'August', 'September', 'October', 'November', 'December']
             }

    return MONTHS[lang][num - 1]

# task E
def to_string(*data, sep=' ', end='\n'):
    string = ''
    data = list(data)
    while data:
        item = data.pop(0)
        string += str(item)
        if data:
            string += sep
    return string + end

# task F
RECIPES = {
    'Эспрессо': {'coffee': 1},
    'Капучино': {"coffee": 1, "milk": 3},
    'Макиато': {"coffee": 2, "milk": 1},
    'Кофе по-венски': {"coffee": 1, "cream": 2},
    'Латте Макиато': {"coffee": 1, "milk": 2, "cream": 1},
    'Кон Панна': {"coffee": 1, "cream": 1}
}

in_stock = {}


def order(*drinks):
    global in_stock, RECIPES

    for drink in drinks:
        if all(RECIPES[drink][ingredient] <= in_stock[ingredient] for ingredient in RECIPES[drink]):
            for ingredient, amount in RECIPES[drink].items():
                in_stock[ingredient] -= amount
            return drink

    return "К сожалению, не можем предложить Вам напиток"

# task G
data = []
odds = []
evens = []


def enter_results(*numbers):
    global data, odds, evens
    data.extend(list(numbers))
    odds = data[::2]
    evens = data[1::2]


def get_sum():
    return round(sum(odds), 2), round(sum(evens), 2)


def get_average():
    return round(sum(odds) / len(odds), 2), round(sum(evens) / len(evens), 2)

# task H
lambda x: (len(x), x.lower())

# task I
lambda c: (sum(int(x) for x in str(c)) % 2 == 0)

# task J
def secret_replace(text, **code):
    new_text = ''
    for char in text:
        if char in code:
            new_text += code[char][0]
            code[char] = code[char][1:] + (code[char][0],)
        else:
            new_text += char
    return new_text

