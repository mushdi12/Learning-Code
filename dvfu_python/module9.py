# task A
from sys import stdin

summa = 0
for line in stdin.readlines():
    for item in line.split():
        summa += int(item)

print(summa)

# task B
from sys import stdin

strings = stdin.read().split('\n')
delta = 0
count = 0

for string in strings:
    if string:
        _, then, now = string.split()
        delta += int(now) - int(then)
        count += 1

print(round(delta / count))

# task C
from sys import stdin

for string in stdin.readlines():
    if string == '\n':
        print(string)
    elif string.strip()[0] != '#':
        if (pos := string.find('# ')) + 1:
            string = string[:pos]
        print(string.strip('\n'))

# task D
from sys import stdin

lines = stdin.readlines()
subject = lines[-1].strip('\n').lower()
objects = lines[:-1]

for line in objects:
    if line.lower().find(subject) + 1:
        print(line.strip('\n'))

# task E
from sys import stdin

words = []
strings = stdin.readlines()

for string in strings:
    for word in string.replace('\n', '').split():
        if word.upper() == word.upper()[::-1]:
            words.append(word)

print('\n'.join(sorted(set(words))))

# task F
alphabet = {
    'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'E',
    'Ж': 'ZH', 'З': 'Z', 'И': 'I', 'Й': 'I', 'К': 'K', 'Л': 'L', 'М': 'M',
    'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U',
    'Ф': 'F', 'Х': 'KH', 'Ц': 'TC', 'Ч': 'CH', 'Ш': 'SH', 'Щ': 'SHCH',
    'Ы': 'Y', 'Э': 'E', 'Ю': 'IU', 'Я': 'IA', 'Ь': '', 'Ъ': ''
}

with open('transliteration.txt', 'w', encoding='UTF-8') as file_out:
    with open('cyrillic.txt', encoding='UTF-8') as file_in:
        for string in file_in:
            for char in string:
                current = char.upper()
                if current in alphabet:
                    if char.isupper():
                        char = alphabet[current].capitalize()
                    else:
                        char = alphabet[current].lower()
                else:
                    char = char
                print(char, end='', file=file_out)

# task G
with open(input(), encoding='UTF-8') as file_in:
    numbers = [int(number) for number in file_in.read().split()]

print(length := len(numbers))
print(len([number for number in numbers if number > 0]))
print(min(numbers))
print(max(numbers))
print(total := sum(numbers))
print(f'{(total / length):.2f}')

# task H
file_1 = input()
file_2 = input()
file_out = input()

with open(file_1, encoding='UTF-8') as file_in:
    items_1 = set([item for item in file_in.read().split()])
with open(file_2, encoding='UTF-8') as file_in:
    items_2 = set([item for item in file_in.read().split()])

unique = items_1 ^ items_2

with open(file_out, 'w', encoding='UTF-8') as file_name:
    print('\n'.join(sorted(unique)), file=file_name)

# task I
file_in = input()
file_out = input()

with open(file_in, encoding="UTF-8") as file_in:
    text = file_in.read()

while text.find("\t") + 1:
    text = text.replace("\t", "")
while text.find("  ") + 1:
    text = text.replace("  ", " ")

text = "\n".join(string.strip() for string in text.split("\n") if string)

with open(file_out, "w", encoding="UTF-8") as file_out:
    file_out.write(text)

# task J
file_name = input()
lines = int(input())

data = []
with open(file_name) as file:
    for string in file:
        data.append(string)
for string in data[-lines:]:
    print(string.strip())

# task K
import json

file_in = input().strip()
file_out = input().strip()

with open(file_in, encoding="UTF-8") as file:
    numbers = [int(number) for number in file.read().split()]

stat = {
    "count": (length := len(numbers)),
    "positive_count": len([number for number in numbers if number > 0]),
    "min": min(numbers),
    "max": max(numbers),
    "sum": (total := sum(numbers)),
    "average": round(total / length, 2),
}

with open(file_out, "w", encoding="UTF-8") as file:
    json.dump(stat, file, ensure_ascii=False, indent=4)

# task L
input_file = input()
evens_file = input()
odds_file = input()
equals_file = input()

with open(input_file, encoding="UTF-8") as file:
    strings = [string for string in file.read().split("\n") if string]

even_digits = "02468"
odd_digits = "13579"

for string in strings:
    evens, odds, equals = [], [], []

    for number in string.split():
        total_evens = total_odds = 0
        for char in number:
            if char in even_digits:
                total_evens += 1
            elif char in odd_digits:
                total_odds += 1

        if total_evens > total_odds:
            evens.append(number)
        elif total_evens < total_odds:
            odds.append(number)
        else:
            equals.append(number)

    with open(evens_file, "a", encoding="UTF-8") as file:
        file.write(" ".join(evens) + "\n")
    with open(odds_file, "a", encoding="UTF-8") as file:
        file.write(" ".join(odds) + "\n")
    with open(equals_file, "a", encoding="UTF-8") as file:
        file.write(" ".join(equals) + "\n")

# task M
from sys import stdin
import json

json_name = input()

with open(json_name) as file:
    data = json.load(file)

lines = stdin.readlines()

for line in lines:
    if line:
        key, value = line.split('==')
        data[key.strip()] = value.strip()

with open(json_name, 'w') as file:
    json.dump(data, file, sort_keys=False, indent=4, ensure_ascii=False)

# task N
import json

json_name = input()
json_update = input()

with open(json_name) as file:
    source = json.load(file)
with open(json_update) as file:
    updates = json.load(file)

name_key = 'name'
new_dict = {}

for update in updates:
    for data in source:
        if update[name_key] == data[name_key]:
            for key in update.keys():
                if update[key] > data.get(key, ''):
                    data[key] = update[key]

for data in source:
    name = data.pop(name_key)
    new_dict[name] = data

with open(json_name, 'w') as file:
    json.dump(new_dict, file, sort_keys=False, indent=4, ensure_ascii=False)

# task O
from sys import stdin
import json

json_name = 'scoring.json'

with open(json_name) as file:
    data = json.load(file)

answers = stdin.readlines()

score = 0

while data:
    tests = data.pop(0)
    multiplier = int(tests['points'] / len(tests['tests']))
    for test in tests['tests']:
        result = test['pattern']
        answer = answers.pop(0).strip('\n')
        if result == answer:
            score += multiplier

print(score)

# task P
from sys import stdin

search_for, *file_names = [string.strip() for string in stdin]

found = False

for file_name in file_names:
    with open(file_name, encoding='UTF-8') as file:
        data = ' '.join(file.read().replace(' ', ' ').lower().split())

        if search_for.lower() in data:
            print(file_name)
            found = True

if not found:
    print('404. Not Found')

# task Q
file_name = 'secret.txt'

with open(file_name, encoding='UTF-8') as file:
    data = file.read()
    decoded = ''
    for char in data:
        code = ord(char)
        code = code % 256 if code >= 128 else code
        decoded += chr(code)

    print(decoded)

# task R
file_name = input()

with open(file_name, 'rb') as file:
    data = file.read()
size = len(data)

scale = ['Б', 'КБ', 'МБ', 'ГБ', 'ТБ']
weight = 0

while size > 1024 and weight < len(scale):
    weight += 1
    size, overload = divmod(size, 1024)
    size += int(overload > 0)

print(f'{size}{scale[weight]}')

# task S
file_in = 'public.txt'
file_out = 'private.txt'

a = ord('a')
z = ord('z')

shift = int(input()) % 26

with open(file_in, encoding='UTF-8') as file:
    data = file.read()

    output = ''

    for i in range(len(data)):
        pos = a
        if a <= (code := ord(data[i].lower())) <= z:
            pos = code + shift
            if pos > z:
                pos -= 26
            elif pos < a:
                pos += 26
            output += chr(pos).upper() if data[i].isupper() else chr(pos)
        else:
            output += data[i]

with open(file_out, 'w', encoding='UTF-8') as file:
    file.write(output)

# task T
file_in = 'numbers.num'
sum = 0

with open(file_in, 'rb') as file:
    while (chunk := file.read(2)):
        sum += int.from_bytes(chunk)

print(sum % 0x10000)
