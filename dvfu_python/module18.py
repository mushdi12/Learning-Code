# task A
import requests


try:
    response = requests.get('http://127.0.0.1:5000')
    response.raise_for_status()
    print(response.text)
except requests.exceptions.RequestException as e:
    print(f"Ошибка при запросе к серверу: {e}")

# task B
import requests

server_address = input().strip()

total_sum = 0
while True:
    try:
        response = requests.get(f'http://{server_address}')
        response.raise_for_status()

        number = int(response.text.strip())

        if number == 0:
            break

        total_sum += number

    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе к серверу: {e}")
        break

print(total_sum)

# task C
import requests

server_address = input().strip()

try:
    response = requests.get(f'http://{server_address}')
    response.raise_for_status()

    data = response.json()

    total_sum = sum(x for x in data if isinstance(x, (int, float)))

    print(total_sum)

except requests.exceptions.RequestException as e:
    print(f"Ошибка при запросе к серверу: {e}")

# task D
import requests

server_address = input().strip()
key = input().strip()

try:
    response = requests.get(f'http://{server_address}')
    response.raise_for_status()

    data = response.json()

    if key in data:
        print(data[key])
    else:
        print("No data")

except requests.exceptions.RequestException as e:
    print(f"Ошибка при запросе к серверу: {e}")
except ValueError:
    print("Ошибка при обработке JSON-данных")

# task E
import requests

server_address = input().strip()
paths = []
while True:
    try:
        path = input().strip()
        if path:
            paths.append(path)
        else:
            break
    except EOFError:
        break

total_sum = 0

for path in paths:
    try:

        response = requests.get(f'http://{server_address}{path}')
        response.raise_for_status()

        data = response.json()

        total_sum += sum([item for item in data if isinstance(item, (int, float))])

    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе к серверу: {e}")
    except ValueError:
        print("Ошибка при обработке JSON-данных")

print(total_sum)

# task F
import requests


server_address = input().strip()

response = requests.get(f'http://{server_address}/users')

if response.status_code == 200:
    users = response.json()

    users.sort(key=lambda user: (user['last_name'], user['first_name']))

    for user in users:
        print(f"{user['last_name']} {user['first_name']}")
else:
    print("Ошибка при получении данных с сервера.")

# task G
import requests


server_address = input().strip()
user_id = input().strip()
message_template = []
while True:
    try:
        line = input()
        message_template.append(line)
    except EOFError:
        break

try:
    response = requests.get(f'http://{server_address}/users/{user_id}')
    response.raise_for_status()
    user_data = response.json()
except requests.exceptions.RequestException:
    print('Пользователь не найден')
    exit()

formatted_message = '\n'.join(
    line.format(**user_data) for line in message_template
)
print(formatted_message)

# task H
import requests
import json


server_address = input().strip()
username = input().strip()
last_name = input().strip()
first_name = input().strip()
email = input().strip()

user_data = {
    "username": username,
    "last_name": last_name,
    "first_name": first_name,
    "email": email
}

response = requests.post(f'http://{server_address}/users', json=user_data)


# task I
import requests

server_address = input().strip()
user_id = int(input().strip())

data = {}
try:
    while True:
        line = input().strip()
        if line:
            key, value = line.split('=')
            data[key] = value
        else:
            break
except EOFError:
    pass

try:
    response = requests.put(f'http://{server_address}/users/{user_id}', json=data)
    response.raise_for_status()

except requests.exceptions.RequestException as e:
    print(f"Ошибка при запросе к серверу: {e}")

# task J
import requests

server_address = input().strip()
user_id = input().strip()

url = f"http://{server_address}/users/{user_id}"

response = requests.delete(url)

if response.status_code == 200 or response.status_code == 204:
    print("Пользователь успешно удален.")
else:
    print(f"Ошибка: {response.status_code}, {response.text}")



