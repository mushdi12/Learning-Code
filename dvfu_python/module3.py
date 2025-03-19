# task A
while input() != "Три!":
    print("Режим ожидания...")
print("Ёлочка, гори!")

# task B
count = 0
while True:
    line = input().strip()
    if line == "Приехали!":
        break
    if "зайка" in line:
        count += 1
print(count)

# task C
start = int(input())
end = int(input())
current = start
while current <= end:
    print(current, end=" ")
    current += 1

# task D
start = int(input())
end = int(input())
step = 0
if start <= end:
    step = 1
else:
    step = -1
current = start
while current != end + step:
    print(current, end=" ")
    current += step

# task E
total = 0
while True:
    price = float(input())
    if price == 0:
        break
    if price >= 500:
        price *= 0.9
    total += price
print(round(total, 1))

# task F
a = int(input())
b = int(input())

while b != 0:
    a, b = b, a % b

print(a)

# task G
a = int(input())
b = int(input())

original_a = a
original_b = b

while b != 0:
    a, b = b, a % b

gcd = a
lcm = (original_a * original_b) // gcd

print(lcm)

# task H
info = input()
n = int(input())

for _ in range(n):
    print(info)

# task I
n = int(input())

factorial = 1
for i in range(1, n + 1):
    factorial *= i

print(factorial)

# task J
x, y = 0, 0

while True:
    direction = input()
    if direction == "СТОП":
        break
    steps = int(input())

    if direction == "СЕВЕР":
        y += steps
    elif direction == "ЮГ":
        y -= steps
    elif direction == "ВОСТОК":
        x += steps
    elif direction == "ЗАПАД":
        x -= steps
print(y)
print(x)

# task K
n = input()
sum_digits = 0

for digit in n:
    sum_digits += int(digit)

print(sum_digits)

# task L
n = input()
max_digit = 0

for digit in n:
    max_digit = max(max_digit, int(digit))

print(max_digit)

# task M
N = int(input())
players = []

for _ in range(N):
    players.append(input().strip())

first_player = min(players)
print(first_player)

# task N
n = int(input())

if n <= 1:
    print("NO")
else:
    is_prime = True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            is_prime = False
            break

    if is_prime:
        print("YES")
    else:
        print("NO")

# task O
n = int(input())
count = 0

for _ in range(n):
    line = input()
    if "зайка" in line:
        count += 1

print(count)

# task P
number = input()

if number == number[::-1]:
    print("YES")
else:
    print("NO")

# task Q
number = input()
result = ''

for digit in number:
    if int(digit) % 2 != 0:
        result += digit

print(result)

# task R
n = int(input())
factors = []
divisor = 2

while divisor * divisor <= n:
    while n % divisor == 0:
        factors.append(divisor)
        n //= divisor
    divisor += 1

if n > 1:
    factors.append(n)

for i in range(len(factors)):
    if i == len(factors) - 1:
        print(factors[i])
    else:
        print(factors[i], end=" * ")

# task S
low = 1
high = 1000
attempts = 0

while attempts < 10:
    guess = (low + high) // 2
    print(guess)
    response = input().strip()

    if response == "Угадал!":
        break
    elif response == "Больше":
        low = guess + 1
    elif response == "Меньше":
        high = guess - 1

    attempts += 1

# task T
N = int(input())
blocks = []

for _ in range(N):
    blocks.append(int(input()))

previous_hash = 0

for i in range(N):
    b = blocks[i]

    m = b // (256 * 256)
    r = (b // 256) % 256
    h = b % 256

    calculated_hash = (37 * (m + r + previous_hash)) % 256

    if h >= 100 or h != calculated_hash:
        print(i)
        break
    previous_hash = h
else:
    print(-1)

