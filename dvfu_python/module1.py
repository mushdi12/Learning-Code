# task A
print("Привет, Яндекс!")

# task B
print(f"Привет, " + input('Как Вас зовут?\n'))

# task C
input_line = input()
for _ in range(3):
    print(input_line)

# task D
input_money = int(input())
print(int(input_money - 2.5 * 38))

# task E
product_price = int(input())
product_weight = int(input())
user_money = int(input())
print(int(user_money - product_price * product_weight))

# task F
product_name = input()
product_price = int(input())
product_weight = int(input())
user_money = int(input())

print("Чек")
print(f"{product_name} - {product_weight}кг - {product_price}руб/кг")
print(f"Итого: {product_weight * product_price}руб")
print(f"Внесено: {user_money}руб")
print(f"Сдача: {user_money - product_weight * product_price}руб")

# task G
cnt = int(input())
for i in range(cnt):
    print("Купи слона!")

# task H
cnt = int(input())
input_line = input()
for i in range(cnt):
    print(f'Я больше никогда не буду писать "{input_line}"!')

# task I
child_cnt = int(input())
minutes = int(input())
print(child_cnt * minutes // 2)

# task J
child_name = input()
locker_number = input()

group_number = locker_number[0]
bed_number = locker_number[1]
child_number = locker_number[2]

print(f"Группа №{group_number}.")
print(f"{child_number}. {child_name}.")
print(f"Шкафчик: {locker_number}.")
print(f"Кроватка: {bed_number}.")

# task K
numbers = input()

print(f"{numbers[1]}{numbers[0]}{numbers[3]}{numbers[2]}")

# task L
num1 = input().zfill(3)
num2 = input().zfill(3)

result = ""
for a, b in zip(num1, num2):
    result += str((int(a) + int(b)) % 10)

print(int(result))

# task M
children_count = int(input())
candies_count = int(input())

print(candies_count // children_count)
print(candies_count % children_count)

# task N
r = int(input())
g = int(input())
b = int(input())
print(r + b + 1)

# task O
N = int(input())
M = int(input())
T = int(input())

total_minutes = N * 60 + M + T

result_hours = (total_minutes // 60) % 24
result_minutes = total_minutes % 60
print(f"{result_hours:02}:{result_minutes:02}")

# task P
a = int(input())
b = int(input())
c = int(input())
print((abs(b - a)) / c)

# task Q
decimal_sum = int(input())
binary_sum = int(input(), 2)

print(decimal_sum + binary_sum)

# task R
binary_price = int(input(), 2)
cash_given = int(input())
print(cash_given - binary_price)

# task S
product_name = input()
product_price = int(input())
product_weight = int(input())
user_money = int(input())

total_cost = product_price * product_weight
change = user_money - total_cost

print("=" * 16 + "Чек" + "=" * 16)
print("Товар:".ljust(35 - len(product_name)) + product_name)
print("Цена:".ljust(
    35 - 11 - len(str(product_weight)) - len(str(product_price))) + f"{product_weight}кг * {product_price}руб/кг")
print("Итого:".ljust(35 - len(str(total_cost)) - 3) + f"{total_cost}руб")
print("Внесено:".ljust(35 - len(str(user_money)) - 3) + f"{user_money}руб")
print("Сдача:".ljust(35 - len(str(change)) - 3) + f"{change}руб")
print("=" * 35)

# task T
N = int(input())
M = int(input())
K1 = int(input())
K2 = int(input())

first_weight = (M * N - K2 * N) // (K1 - K2)
second_weight = N - first_weight

print(first_weight, second_weight)

