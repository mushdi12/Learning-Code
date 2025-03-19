# task A
for index, word in enumerate(input().split(), start=1):
    print(f'{index}. {word}')

# task B
left = input().split(', ')
right = input().split(', ')

for kids in zip(left, right):
    print(f'{kids[0]} - {kids[1]}')

# task C
from itertools import count

start, stop, step = [float(x) for x in input().split()]

for num in count(start, step):
    if num >= stop:
        break
    print(f'{num:.2f}')

# task D
from itertools import accumulate

for string in accumulate([word + ' ' for word in input().split()]):
    print(string)

# task E
from itertools import chain

lst = sorted(set(chain.from_iterable([input().split(", ") for _ in range(3)])))

for index, value in enumerate(lst, 1):
    print(f"{index}. {value}")

# task F
from itertools import product

cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'валет', 'дама', 'король', 'туз']
suits = ['пик', 'треф', 'бубен', 'червей']

suits.remove(input())

for card, suit in product(cards, suits):
    print(card, suit)

# task G
from itertools import combinations

names = [input() for _ in range(int(input()))]

print('\n'.join([f'{name1} - {name2}' for name1, name2 in list(combinations(names, 2))]))

# task H
from itertools import cycle, islice

porridges = [input() for _ in range(int(input()))]

days = int(input())

print('\n'.join(islice(cycle(porridges), days)))

# task I
from itertools import product, islice

size = int(input())

nums = range(1, size + 1)

table = [x * y for x, y in product(nums, repeat=2)]

for row in range(size):
    print(*islice(table, row * size, (row + 1) * size))

# task J
from itertools import product

num = int(input())
nums = range(1, num - 1)
table = list(product(nums, repeat=3))

print('А Б В')
for i in range(len(table)):
    if sum(table[i]) == num:
        print(*table[i])

# task K
from itertools import product

x = int(input())
y = int(input())

ln = len(str(x * y))

for i, j in product(range(1, x + 1), range(1, y + 1)):
    print(f'{((i - 1) * y + j):>{ln}}', end=' ')
    if j == y:
        print()

# task L
string = []

for _ in range(int(input())):
    string.extend(input().split(', '))

lst = enumerate(sorted(string), 1)

print('\n'.join([f'{num}. {item}' for num, item in lst]))

# task M
from itertools import permutations

names = []

for _ in range(num := int(input())):
    names.append(input())

names.sort()

for name_list in permutations(names, num):
    print(', '.join(name_list))

# task N
from itertools import permutations
str = []

for _ in range(num := int(input())):
    str.append(input())

str.sort()

for pos in permutations(str, 3):
    print(', '.join(pos))

# task O
from itertools import permutations
lst = []

for _ in range(num := int(input())):
    lst.extend(input().split(', '))

lst.sort()

for items in permutations(lst, 3):
    print(' '.join(items))

# task P
from itertools import chain, permutations, product

suit = input().strip()
rank = input().strip()

suits = {'буби': 'бубен', 'пики': 'пик', 'трефы': 'треф', 'черви': 'червей'}
ranks = ['10', '2', '3', '4', '5', '6', '7', '8', '9', 'валет', 'дама', 'король', 'туз']

ranks.remove(rank)

deck = product(ranks, suits.values())

triplets = permutations(deck, 3)

triplets = [triplet for triplet in triplets if suits[suit] in chain.from_iterable(triplet)]

sorted_combinations = sorted(triplets)
for combination in sorted_combinations[:10]:
    print(', '.join(f'{rank} {suit}' for rank, suit in combination))

# task Q
from itertools import chain, combinations, product

suit = input().strip()
rank = input().strip()
hand = input()

suits = {'буби': 'бубен', 'пики': 'пик', 'трефы': 'треф', 'черви': 'червей'}
ranks = ['10', '2', '3', '4', '5', '6', '7', '8', '9', 'валет', 'дама', 'король', 'туз']

ranks.remove(rank)

deck = product(ranks, suits.values())

triplets = combinations(deck, 3)
triplets = [triplet for triplet in triplets if suits[suit] in chain.from_iterable(triplet)]
triplets.sort()

print_next = False

for triplet in triplets:
    if print_next:
        print(', '.join(f'{rank} {suit}' for rank, suit in triplet))
        break
    if ', '.join(f'{rank} {suit}' for rank, suit in triplet) == hand:
        print_next = True

# task R
from itertools import product

expression = input()
print('a b c f')
for a, b, c in product([0, 1], repeat=3):
    print(a, b, c, int(eval(expression, {'a': a, 'b': b, 'c': c})))

# task S
from itertools import product

expression = input()

variables = [item for item in sorted(set(expression.split())) if item.isupper()]

length = len(variables)

print(*[v for v in variables], "F")

for values in product([False, True], repeat=length):
    globals = {key: value for key, value in zip(variables, values)}
    print(*[int(v) for v in values], int(eval(expression, globals)))

# task T
from itertools import product

OPERATORS = {
    'not': 'not',
    'and': 'and',
    'or': 'or',
    '^': '!=',
    '->': '<=',
    '~': '==',
}

PRIORITY = {
    'not': 0,
    'and': 1,
    'or': 2,
    '^': 3,
    '->': 4,
    '~': 5,
    '(': 6,
}


def parse_expression(expression, variables):
    stack = []
    result = []

    expression = expression.replace('(', '( ').replace(')', ' )')

    for item in expression.split():
        if item in variables:
            result.append(item)
        elif item == '(':
            stack.append(item)
        elif item == ')':
            while stack[-1] != '(':
                result.append(OPERATORS[stack.pop()])
            stack.pop()
        elif item in OPERATORS:
            while stack and PRIORITY[item] >= PRIORITY[stack[-1]]:
                result.append(OPERATORS[stack.pop()])
            stack.append(item)
    while stack:
        result.append(OPERATORS[stack.pop()])
    return result


def evaluate(expression, variables):
    stack = []
    for item in expression:
        if item in variables:
            stack.append(variables[item])
        else:
            if item == 'not':
                stack.append(not stack.pop())
            else:
                variable2, variable1 = stack.pop(), stack.pop()
                stack.append(eval(f'{variable1} {item} {variable2}'))  # noqa
    return int(stack.pop())


expression = input()
variables = sorted(set([item for item in expression if item.isupper()]))
parsed_expression = parse_expression(expression, variables)
table = product([0, 1], repeat=len(variables))

print(*variables, 'F')
for values in table:
    globals = {key: value for key, value in zip(variables, values)}
    print(*values, evaluate(parsed_expression, globals))

