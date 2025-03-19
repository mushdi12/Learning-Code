# task A
try:
    func()
except ValueError:
    print('ValueError')
except TypeError:
    print('TypeError')
except SystemError:
    print('SystemError')
except Exception as e:
    print('Unexpected error: {e}')
else:
    print('No Exceptions')

# task B
a = 'str'
b = (3, 5)

func(a, b)

# task C
class MyClass:

    def __repr__(self) -> str:
        raise Exception


a = MyClass()
func(a)

# task D
def only_positive_even_sum(*args):
    for item in args:
        if not isinstance(item, int):
            raise TypeError
    for item in args:
        if item <= 0 or item % 2 != 0:
            raise ValueError
    return sum(args)

# task E
def check_queue_iterated(*queues):
    for queue in queues:
        try:
            iter(queue)
        except TypeError:
            raise StopIteration


def check_queue_consistence(*queues):
    queue = []
    for queue_in_queues in queues:
        queue.extend(list(queue_in_queues))
    if not all(type(member) is type(queue[0]) for member in queue):
        raise TypeError


def check_queue_sorted(*queues):
    for queue in queues:
        if list(queue) != sorted(queue):
            raise ValueError


def merge(queue_1, queue_2):
    check_queue_iterated(queue_1, queue_2)
    check_queue_consistence(queue_1, queue_2)
    check_queue_sorted(queue_1, queue_2)
    queue_1n = list(queue_1)
    queue_2n = list(queue_2)
    sequence = []

    while queue_1n and queue_2n:
        if queue_1n[0] > queue_2n[0]:
            sequence.append(queue_2n.pop(0))
        else:
            sequence.append(queue_1n.pop(0))
    sequence.extend(queue_1n + queue_2n)
    return sequence

# task F
class InfiniteSolutionsError(Exception):
    pass


class NoSolutionsError(Exception):
    pass


def find_roots(a, b, c):

    roots = ()

    if not all(type(num) in (int, float) for num in (a, b, c)):
        raise TypeError

    if a == b == c == 0:
        raise InfiniteSolutionsError('Infinite solutions')
    elif a == 0 and b != 0 and c != 0:
        roots = (-(c / b), -(c / b))
    elif a == b == 0:
        raise NoSolutionsError('No solution')
    elif a == c == 0:
        roots = (0, 0)
    else:
        disc = (b ** 2) - (4 * a * c)
        if disc == 0:
            roots = ((-b) / (2 * a), (-b) / (2 * a))
        elif disc > 0:
            x1 = (-b - (disc ** 0.5)) / (2 * a)
            x2 = (-b + (disc ** 0.5)) / (2 * a)
            roots = tuple(sorted([x1, x2]))
        else:
            raise NoSolutionsError('No solution')
    return roots

# task G
class CyrillicError(Exception):
    pass


class CapitalError(Exception):
    pass


def name_validation(name) -> str:
    valid_cyrillic_chars = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    if not isinstance(name, str):
        raise TypeError
    if not all([char.lower() in valid_cyrillic_chars for char in name]):
        raise CyrillicError
    if not name.istitle():
        raise CapitalError
    return name

# task H
class BadCharacterError(Exception):
    pass


class StartsWithDigitError(Exception):
    pass


def username_validation(username) -> str:
    valid_username_chars = 'abcdefghijklmnopqrstuvwxyz_0123456789'
    if not isinstance(username, str):
        raise TypeError
    if not all([char.lower() in valid_username_chars for char in username]):
        raise BadCharacterError
    if username[0].isdigit():
        raise StartsWithDigitError
    return username

# task I
class CyrillicError(Exception):
    pass


class CapitalError(Exception):
    pass


class BadCharacterError(Exception):
    pass


class StartsWithDigitError(Exception):
    pass


def name_validation(name) -> str:
    valid_cyrillic_chars = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    if not isinstance(name, str):
        raise TypeError
    if not all([char.lower() in valid_cyrillic_chars for char in name]):
        raise CyrillicError
    if name.capitalize() != name:
        raise CapitalError
    return name


def username_validation(username) -> str:
    valid_username_chars = 'abcdefghijklmnopqrstuvwxyz_0123456789'
    if not isinstance(username, str):
        raise TypeError
    if not all([char.lower() in valid_username_chars for char in username]):
        raise BadCharacterError
    if username[0].isdigit():
        raise StartsWithDigitError
    return username


def user_validation(*args, **kwargs) -> dict:
    allowed = ['last_name', 'first_name', 'username']
    user = kwargs

    try:
        if any([user[field] == '' for field in allowed]):
            raise KeyError
    except Exception:
        raise KeyError

    if not all([field in allowed for field in user.keys()]):
        raise KeyError

    name_validation(user['last_name'])
    name_validation(user['first_name'])
    username_validation(user['username'])

    return user

# task J
import hashlib


class MinLengthError(Exception):
    pass


class PossibleCharError(Exception):
    pass


class NeedCharError(Exception):
    pass


possible_password_chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'


def password_validation(password, min_length=8,
                        possible_chars=possible_password_chars,
                        at_least_one=str.isdigit) -> str:
    if not isinstance(password, str):
        raise TypeError
    if len(password) < min_length:
        raise MinLengthError
    if any([char not in possible_chars
            for char in password]):
        raise PossibleCharError
    if not any([at_least_one(char) for char in password]):
        raise NeedCharError

    hash_object = hashlib.sha256()
    hash_object.update(password.encode())
    hash = hash_object.hexdigest()

    return hash


