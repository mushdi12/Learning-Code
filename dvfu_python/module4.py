# task A
n = int(input())

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(i * j, end=" " if j < n else "\n")

# task B
n = int(input())

for j in range(1, n + 1):
    for i in range(1, n + 1):
        print(f"{i} * {j} = {i * j}")

# task C
n = int(input())

current = 1
row = 1

while current <= n:
    for _ in range(row):
        if current > n:
            break
        print(current, end=" ")
        current += 1
    print()
    row += 1

# task D
n = int(input())

total_sum = 0

for _ in range(n):
    number = input()
    total_sum += sum(int(digit) for digit in number)

print(total_sum)

# task E
n = int(input())

count_with_rabbit = 0

for _ in range(n):
    has_rabbit = False
    while True:
        word = input()
        if word == "ВСЁ":
            break
        if word == "зайка":
            has_rabbit = True
    if has_rabbit:
        count_with_rabbit += 1

print(count_with_rabbit)


# task F
def find_gcd(a, b):
    while b:
        a, b = b, a % b
    return a


n = int(input())

numbers = [int(input()) for _ in range(n)]

current_gcd = numbers[0]
for num in numbers[1:]:
    current_gcd = find_gcd(current_gcd, num)

print(current_gcd)

# task G
n = int(input())

for i in range(1, n + 1):
    start_time = 3 + (i - 1)
    for t in range(start_time, 0, -1):
        print(f"До старта {t} секунд(ы)")
    print(f"Старт {i}!!!")

# task H
n = int(input())

max_sum = -1
winner_name = ""

for _ in range(n):
    name = input().strip()
    number = input().strip()

    digit_sum = sum(int(digit) for digit in number)

    if digit_sum >= max_sum:
        max_sum = digit_sum
        winner_name = name

print(winner_name)

# task I
n = int(input())

result = ""

for _ in range(n):
    number = input().strip()
    max_digit = max(number)
    result += max_digit

print(result)


# task J
def divide_orange(slices):
    print("\u0410 \u0411 \u0412")
    for a in range(1, slices - 1):
        for b in range(1, slices - a):
            c = slices - a - b
            if c > 0:
                print(a, b, c)


slices = int(input().strip())
divide_orange(slices)


# task K
def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True


n = int(input().strip())
count_primes = 0

for _ in range(n):
    number = int(input().strip())
    if is_prime(number):
        count_primes += 1

print(count_primes)


# task L
def print_number_rectangle(n, m):
    max_num = n * m
    width = len(str(max_num))

    num = 1
    for i in range(n):
        row = []
        for j in range(m):
            row.append(f"{num:>{width}}")
            num += 1
        print(" ".join(row))


n = int(input().strip())
m = int(input().strip())
print_number_rectangle(n, m)


# task M
def print_number_rectangle(n, m):
    max_num = n * m
    width = len(str(max_num))

    for i in range(n):
        row = []
        for j in range(m):
            num = i + 1 + j * n
            row.append(f"{num:>{width}}")
        print(" ".join(row))


n = int(input().strip())
m = int(input().strip())
print_number_rectangle(n, m)


# task N
def print_snake_pattern(n, m):
    max_num = n * m
    width = len(str(max_num))

    num = 1
    for i in range(n):
        row = []
        for j in range(m):
            row.append(f"{num:>{width}}")
            num += 1
        if i % 2 == 1:
            row.reverse()
        print(" ".join(row))


n = int(input().strip())
m = int(input().strip())
print_snake_pattern(n, m)


# task O
def print_snake_pattern(n, m):
    max_num = n * m
    width = len(str(max_num))

    matrix = [[0] * m for _ in range(n)]

    num = 1
    for j in range(m):
        if j % 2 == 0:
            for i in range(n):
                matrix[i][j] = num
                num += 1
        else:
            for i in range(n - 1, -1, -1):
                matrix[i][j] = num
                num += 1

    for row in matrix:
        print(" ".join(f"{x:>{width}}" for x in row))


n = int(input().strip())
m = int(input().strip())
print_snake_pattern(n, m)

# task P
n = int(input())
width = int(input())

cell_format = f"{{:^{width}}}"

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if j == n:
            print(cell_format.format(i * j), end="")
        else:
            print(cell_format.format(i * j), end="|")
    print()

    if i != n:
        print("-" * (width * n + n - 1))


# task Q
def is_palindrome(s):
    return s == s[::-1]


n = int(input().strip())
count_palindromes = 0

for _ in range(n):
    num = input().strip()
    if is_palindrome(num):
        count_palindromes += 1

print(count_palindromes)

# task R
limit = int(input())

counter = 0
width = 1
max_length = 0

while counter <= limit:
    string_length = 0
    for position in range(width):
        counter += 1
        if counter <= limit:
            string_length += len(str(counter))
        if position < width - 1 and counter < limit:
            string_length += 1

    if max_length < string_length:
        max_length = string_length

    width += 1

counter = 0
width = 1

while counter <= limit:
    string = ''
    for position in range(width):
        counter += 1
        if counter <= limit:
            string += str(counter)
        if position < width - 1 and counter < limit:
            string += ' '
    width += 1
    print(f'{string:^{max_length}}')

# task S
size = int(input())

cell_width = len(str((size + 1) // 2))

for i in range(size):
    for j in range(size):
        print(f'{min(i + 1, j + 1, size - i, size - j):>{cell_width}}', end=' ')
    print()


# task T
def sum_of_digits(n, base):
    total_sum = 0
    while n > 0:
        total_sum += n % base
        n //= base
    return total_sum


n = int(input().strip())

max_sum = 0
best_base = 2

for base in range(2, 11):
    current_sum = sum_of_digits(n, base)
    if current_sum > max_sum:
        max_sum = current_sum
        best_base = base

print(best_base)

