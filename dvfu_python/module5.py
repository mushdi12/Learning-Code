# task A
N = int(input())
valid_letters = {'а', 'б', 'в'}

for _ in range(N):
    word = input().strip()
    if word[0] not in valid_letters:
        print("NO")
        break
else:
    print("YES")

# task B
s = input().strip()

for char in s:
    print(char)

# task C
L = int(input())
N = int(input())

for _ in range(N):
    title = input()
    if len(title) > L:
        print(title[:L - 3] + "...")
    else:
        print(title)

# task D
while True:
    line = input().strip()
    if line == "":
        break

    if line.startswith("##"):
        line = line[2:].strip()

    if not line.endswith("@@@"):
        print(line)

# task E
s = input().strip()
if s == s[::-1]:
    print("YES")
else:
    print("NO")

# task F
n = int(input())
count = 0

for _ in range(n):
    words = input().split()
    count += words.count("зайка")

print(count)

# task G
a, b = map(int, input().split())
print(a + b)

# task H
N = int(input())

for _ in range(N):
    line = input()
    position = line.find('зайка')

    if position == -1:
        print('Заек нет =(')
    else:
        print(position + 1)

# task I
while True:
    line = input()
    if line == "":
        break
    clean_line = line.split('#')[0]

    if clean_line:
        print(clean_line)

# task J
from collections import Counter

freq = Counter()

while True:
    line = input().strip()
    if line == "ФИНИШ":
        break
    line = line.replace(" ", "").lower()
    freq.update(line)

most_common = min(freq, key=lambda x: (-freq[x], x))
print(most_common)

# task K
N = int(input())
pages = [input().strip() for _ in range(N)]
query = input().strip().lower()

result = [page for page in pages if query in page.lower()]

print("\n".join(result))

# task L
porridges = ["Манная", "Гречневая", "Пшённая", "Овсяная", "Рисовая"]

N = int(input())

for i in range(N):
    print(porridges[i % 5])

# task M
N = int(input())
numbers = [int(input()) for _ in range(N)]
P = int(input())
for number in numbers:
    print(number ** P)

# task N
numbers = list(map(int, input().split()))
P = int(input())
result = [str(number ** P) for number in numbers]
print(" ".join(result))


# task O
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


numbers = list(map(int, input().split()))
gcd_result = numbers[0]
for number in numbers[1:]:
    gcd_result = gcd(gcd_result, number)

print(gcd_result)

# task P
L = int(input())
N = int(input())
headlines = [input() for i in range(N)]

result = []
current_length = 0

for line in headlines:
    line_length = len(line)

    if current_length + line_length <= L:
        result.append(line)
        current_length += line_length
    else:
        remaining_space = L - current_length
        if remaining_space > 3:
            truncated_line = line[:remaining_space - 3] + "..."
            if truncated_line[-4] == ',':
                truncated_line = truncated_line[:-4] + "..."
            result.append(truncated_line)
        else:
            truncated_line = result[-1][:L - 3] + "..."
            if truncated_line[-4] == ',':
                truncated_line = truncated_line[:-4] + "..."
            result[-1] = truncated_line
        break

print("\n".join(result))

# task Q
s = input().strip().lower()
s = s.replace(' ', '')

if s == s[::-1]:
    print("YES")
else:
    print("NO")

# task R
s = input().strip()

count = 1
for i in range(1, len(s)):
    if s[i] == s[i - 1]:
        count += 1
    else:
        print(s[i - 1], count)
        count = 1
print(s[-1], count)

# task S
expression = input().split()

stack = []

for token in expression:
    if token.isdigit() or (token[0] == '-' and token[1:].isdigit()):
        stack.append(int(token))
    else:
        b = stack.pop()
        a = stack.pop()
        if token == '+':
            stack.append(a + b)
        elif token == '-':
            stack.append(a - b)
        elif token == '*':
            stack.append(a * b)

print(stack[0])

# task T
import math


def factorial(n):
    if n < 0:
        return 0  # Факториал от отрицательного числа не существует
    return math.factorial(n)


expression = input().split()
stack = []

for token in expression:
    if token.isdigit() or (token[0] == '-' and token[1:].isdigit()):
        stack.append(int(token))
    elif token == '+':
        b = stack.pop()
        a = stack.pop()
        stack.append(a + b)
    elif token == '-':
        b = stack.pop()
        a = stack.pop()
        stack.append(a - b)
    elif token == '*':
        b = stack.pop()
        a = stack.pop()
        stack.append(a * b)
    elif token == '/':
        b = stack.pop()
        a = stack.pop()
        stack.append(a // b)
    elif token == '~':
        a = stack.pop()
        stack.append(-a)
    elif token == '!':
        a = stack.pop()
        stack.append(factorial(a))
    elif token == '#':
        a = stack.pop()
        stack.append(a)
        stack.append(a)
    elif token == '@':
        c = stack.pop()
        b = stack.pop()
        a = stack.pop()
        stack.append(b)
        stack.append(c)
        stack.append(a)

print(stack[0])


