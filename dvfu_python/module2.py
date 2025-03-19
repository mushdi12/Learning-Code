# task A
print("Как Вас зовут?")
name = input()
print(f"Здравствуйте, {name}!")
print("Как дела?")
mood = input()
if mood == "хорошо":
    print("Я за вас рада!")
elif mood == "плохо":
    print("Всё наладится!")

# task B
p = int(input())
v = int(input())
if p > v:
    print("Петя")
else:
    print("Вася")

# task C
speed_pety = int(input())
speed_vasya = int(input())
speed_tolya = int(input())

if speed_pety > speed_vasya and speed_pety > speed_tolya:
    print("Петя")
elif speed_vasya > speed_pety and speed_vasya > speed_tolya:
    print("Вася")
else:
    print("Толя")

# task Dspeed_pety = int(input())
speed_vasya = int(input())
speed_tolya = int(input())

if speed_pety > speed_vasya and speed_pety > speed_tolya:
    print("1. Петя")
    if speed_vasya > speed_tolya:
        print("2. Вася")
        print("3. Толя")
    else:
        print("2. Толя")
        print("3. Вася")
elif speed_vasya > speed_pety and speed_vasya > speed_tolya:
    print("1. Вася")
    if speed_pety > speed_tolya:
        print("2. Петя")
        print("3. Толя")
    else:
        print("2. Толя")
        print("3. Петя")
else:
    print("1. Толя")
    if speed_pety > speed_vasya:
        print("2. Петя")
        print("3. Вася")
    else:
        print("2. Вася")
        print("3. Петя")

# task E
N = int(input())
M = int(input())

pety_apple = 7
vasya_apple = 6

pety_apple = pety_apple - 3 + 2 + N
vasya_apple = vasya_apple + 3 - 5 + 2 + M

if pety_apple > vasya_apple:
    print("Петя")
else:
    print("Вася")

# task F
year = int(input())

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("YES")
else:
    print("NO")

# task G
number = input().strip()

if number == number[::-1]:
    print("YES")
else:
    print("NO")

# task H
sentence = input().strip()

if "зайка" in sentence.split():
    print("YES")
else:
    print("NO")

# task I
names = [input().strip() for _ in range(3)]
print(min(names))

# task J
num = input().strip()
a = int(num[0]) + int(num[1])
b = int(num[1]) + int(num[2])
print(f"{max(a, b)}{min(a, b)}")

# task K
num = input().strip()
digits = [int(digit) for digit in num]

min_digit = min(digits)
max_digit = max(digits)
middle_digit = sum(digits) - min_digit - max_digit

if min_digit + max_digit == middle_digit * 2:
    print("YES")
else:
    print("NO")

# task L
a = int(input())
b = int(input())
c = int(input())

if a + b > c and a + c > b and b + c > a:
    print("YES")
else:
    print("NO")

# task M
a = input().strip()
b = input().strip()
c = input().strip()

for i in range(2):
    if a[i] == b[i] == c[i]:
        print(a[i])
        break

# task N
number = input().strip()
a = int(number[0] + number[1])
b = int(number[1] + number[0])

c = int(number[0] + number[2])
d = int(number[2] + number[0])

e = int(number[1] + number[2])
f = int(number[2] + number[1])

a = [a, b, c, d, e, f]
for i in a:
    if i < 10:
        a.remove(i)
print(min(a), max(a))

# task O
a = input().strip()
b = input().strip()

n1, n2 = int(a[0]), int(b[0])
n3, n4 = int(a[1]), int(b[1])

max_digit = n1
min_digit = n1

if n2 > max_digit:
    max_digit = n2
if n3 > max_digit:
    max_digit = n3
if n4 > max_digit:
    max_digit = n4

if n2 < min_digit:
    min_digit = n2
if n3 < min_digit:
    min_digit = n3
if n4 < min_digit:
    min_digit = n4

digits = [n1, n2, n3, n4]
digits.remove(max_digit)
digits.remove(min_digit)
middle_sum = digits[0] + digits[1]

if len(str(middle_sum)) < 2:
    middle_sum = middle_sum
else:
    middle_sum = str(middle_sum)[1:]

result = str(max_digit) + str(middle_sum) + str(min_digit)

print(result)

# task P
a = int(input())
b = int(input())
c = int(input())

first = ""
second = ""
third = ""

if a > b and a > c:
    first = "Петя"
    if b > c:
        second = "Вася"
        third = "Толя"
    else:
        second = "Толя"
        third = "Вася"
elif b > a and b > c:
    first = "Вася"
    if a > c:
        second = "Петя"
        third = "Толя"
    else:
        second = "Толя"
        third = "Петя"
else:
    first = "Толя"
    if a > b:
        second = "Петя"
        third = "Вася"
    else:
        second = "Вася"
        third = "Петя"

print(first.rjust(14))
print("  " + second.ljust(18))
print(third.rjust(22))
print("   II      I      III   ")

# task Q
import math

a = float(input())
b = float(input())
c = float(input())

if a == 0:
    if b == 0:
        if c == 0:
            print("Infinite solutions")
        else:
            print("No solution")
    else:
        x = -c / b
        print(f"{x:.2f}")
else:
    D = b * b - 4 * a * c
    if D < 0:
        print("No solution")
    elif D == 0:
        x = -b / (2 * a)
        print(f"{x:.2f}")
    else:
        sqrt_D = math.sqrt(D)
        x1 = (-b - sqrt_D) / (2 * a)
        x2 = (-b + sqrt_D) / (2 * a)
        x1, x2 = sorted([x1, x2])
        print(f"{x1:.2f} {x2:.2f}")

# task R
a = int(input())
b = int(input())
c = int(input())

sides = sorted([a, b, c])
a, b, c = sides[0], sides[1], sides[2]

if a ** 2 + b ** 2 == c ** 2:
    print("100%")
elif a ** 2 + b ** 2 < c ** 2:
    print("велика")
else:
    print("крайне мала")

# task Sx = float(input())
y = float(input())

distance = (x ** 2 + y ** 2) ** 0.5

if distance <= 5:
    print("Опасность! Покиньте зону как можно скорее!")
elif distance <= 10:
    print("Зона безопасна. Продолжайте работу.")
else:
    print("Вы вышли в море и рискуете быть съеденным акулой!")

# task T
lines = []
for _ in range(3):
    line = input().strip()
    lines.append(line)

filtered_lines = []
for line in lines:
    if "зайка" in line:
        filtered_lines.append(line)

if filtered_lines:
    best_line = min(filtered_lines)
    print(f"{best_line} {len(best_line)}")
else:
    print("Зайка не найдена")

