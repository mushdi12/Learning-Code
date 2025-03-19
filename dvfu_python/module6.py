# task A
input_string = input().strip()

unique_chars = set(input_string)

print(''.join(unique_chars))

# task B
str1 = input().strip()
str2 = input().strip()

set1 = set(str1)
set2 = set(str2)

common_chars = set1 & set2

print(''.join(common_chars))

# task C
N = int(input())
objects = set()

for _ in range(N):
    objects.update(input().split())

for obj in sorted(objects):
    print(obj)

# task D
N = int(input())
M = int(input())

mannaya = set()
for _ in range(N):
    mannaya.add(input().strip())

ovsyanaya = set()
for _ in range(M):
    ovsyanaya.add(input().strip())

common = mannaya & ovsyanaya

if common:
    print(len(common))
else:
    print("Таких нет")

# task E
list1size = int(input())
list2size = int(input())

porridge_eaters = {}

for _ in range(list1size + list2size):
    eater = input()
    porridge_eaters[eater] = porridge_eaters.get(eater, 0) + 1

one_porridge_lovers = []

for eater in porridge_eaters:
    if porridge_eaters[eater] == 1:
        one_porridge_lovers.append(eater)

if len(one_porridge_lovers) != 0:
    print(len(one_porridge_lovers))
else:
    print('Таких нет')

# task F
N = int(input())
M = int(input())

mannaya = set()
ovsyanaya = set()

for _ in range(N + M):
    surname = input().strip()
    if surname in mannaya:
        ovsyanaya.add(surname)
    else:
        mannaya.add(surname)

common = mannaya & ovsyanaya

only_one_kasha = (mannaya - common) | (ovsyanaya - common)

if only_one_kasha:
    for surname in sorted(only_one_kasha):
        print(surname)
else:
    print("Таких нет")

# task G
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'
}


text = input()


words = text.split()
for word in words:
    morse_word = ' '.join(MORSE_CODE_DICT[char.upper()] for char in word)
    print(morse_word)

# task H
N = int(input())
children = []

for _ in range(N):
    line = input().split()
    surname = line[0]
    favorite_cereals = set(line[1:])
    children.append((surname, favorite_cereals))

target_cereal = input()

result = sorted([surname for surname, cereals in children if target_cereal in cereals])

if result:
    print("\n".join(result))
else:
    print("Таких нет")

# task I
from collections import defaultdict

count = defaultdict(int)

while True:
    line = input().strip()
    if not line:
        break
    words = line.split()
    for word in words:
        count[word] += 1

for word, cnt in count.items():
    print(f"{word} {cnt}")

# task J
translit_dict = {
    'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'e', 'ж': 'zh', 'з': 'z', 'и': 'i', 'й': 'i',
    'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f',
    'х': 'kh', 'ц': 'tc', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ы': 'y', 'э': 'e', 'ю': 'iu', 'я': 'ia',

    'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'E', 'Ж': 'Zh', 'З': 'Z', 'И': 'I', 'Й': 'I',
    'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U', 'Ф': 'F',
    'Х': 'Kh', 'Ц': 'Tc', 'Ч': 'Ch', 'Ш': 'Sh', 'Щ': 'Shch', 'Ы': 'Y', 'Э': 'E', 'Ю': 'Iu', 'Я': 'Ia'
}

text = input().strip()

result = []
for char in text:
    if char in translit_dict:
        result.append(translit_dict[char])
    elif char in 'ъъьЬЪ':
        continue
    else:
        result.append(char)

print("".join(result))

# task K
n = int(input())
surnames = [input().strip() for _ in range(n)]

surname_count = {}

for surname in surnames:
    if surname in surname_count:
        surname_count[surname] += 1
    else:
        surname_count[surname] = 1

one_family_count = 0
for count in surname_count.values():
    if count > 1:
        one_family_count += count

print(one_family_count)

# task L
n = int(input())
surnames = [input().strip() for _ in range(n)]

surname_count = {}

for surname in surnames:
    if surname in surname_count:
        surname_count[surname] += 1
    else:
        surname_count[surname] = 1

one_family = [(surname, count) for surname, count in surname_count.items() if count > 1]

if one_family:
    one_family.sort()
    for surname, count in one_family:
        print(f"{surname} - {count}")
else:
    print("Однофамильцев нет")

# task M
n = int(input())
available_dishes = {input().strip() for _ in range(n)}

m = int(input())
cooked_dishes = set()

for _ in range(m):
    day_dishes_count = int(input())
    for _ in range(day_dishes_count):
        cooked_dishes.add(input().strip())

dishes_to_cook = sorted(available_dishes - cooked_dishes)

if dishes_to_cook:
    print("\n".join(dishes_to_cook))
else:
    print("Готовить нечего")

# task N
n = int(input())
available_products = {input().strip() for _ in range(n)}

m = int(input())
recipes_to_cook = []

for _ in range(m):
    dish_name = input().strip()
    k = int(input())
    ingredients = {input().strip() for _ in range(k)}

    if ingredients.issubset(available_products):
        recipes_to_cook.append(dish_name)

if recipes_to_cook:
    print("\n".join(sorted(recipes_to_cook)))
else:
    print("Готовить нечего")

# task O
numbers = input().split()

statistics = []

for num in numbers:
    binary_rep = bin(int(num))[2:]

    digits = len(binary_rep)

    units = binary_rep.count('1')

    zeros = digits - units

    statistics.append({
        "digits": digits,
        "units": units,
        "zeros": zeros
    })

print(statistics)

# task P
lines = []
while True:
    line = input().strip()
    if not line:
        break
    lines.append(line)

adjacent_objects = set()

for line in lines:
    words = line.split()
    for i in range(len(words)):
        if words[i] == "зайка":
            if i > 0:
                adjacent_objects.add(words[i - 1])
            if i < len(words) - 1:
                adjacent_objects.add(words[i + 1])

if adjacent_objects:
    print("\n".join(sorted(adjacent_objects)))
else:
    print("")

# task Q
friends = {}

while pair := input():
    friend1, friend2 = pair.split()
    friends[friend1] = friends.get(friend1, set()) | set([friend2])
    friends[friend2] = friends.get(friend2, set()) | set([friend1])

friends_of_friends = {}

for name in sorted(friends):
    for person in friends[name]:
        friends_of_friends[name] = friends_of_friends.get(
            name, set()) | friends[person]

for name in friends_of_friends:
    friends_of_friends[name].discard(name)
    friends_of_friends[name] -= friends[name]
    friends_of_friends[name] = sorted(friends_of_friends[name])

    print(f'{name}: {", ".join(friends_of_friends[name])}')

# task R
treasures = dict()

for _ in range(count := int(input())):
    x, y = input().split()
    index = (int(x) // 10, int(y) // 10)
    treasures[index] = treasures.get(index, 0) + 1

print(max(treasures.values()))

# task S
from collections import Counter

n = int(input())
toy_count = Counter()
toys_by_child = []

for _ in range(n):
    line = input().strip()
    name, toys = line.split(": ")
    toys_list = toys.split(", ")
    toys_by_child.append(set(toys_list))
    toys_list = set(toys_list)
    toy_count.update(toys_list)

unique_toys = []
for toy, count in toy_count.items():
    if count == 1:
        for toys in toys_by_child:
            if toy in toys:
                unique_toys.append(toy)
                break

unique_toys.sort()
for toy in unique_toys:
    print(toy)

# task T
items = set(input().split('; '))

numbers = []

for item in items:
    numbers.append(int(item))

numbers.sort()

for num1 in numbers:
    mutually = []
    for num2 in numbers:
        if num1 != num2:
            a, b = num1, num2
            while b != 0:
                a, b = b, a % b
            if a == 1:
                mutually.append(str(num2))
    if mutually:
        print(num1, '-', ", ".join(mutually))
