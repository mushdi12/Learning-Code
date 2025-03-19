# task A
def recursive_sum(*nums):
    if not nums:
        return 0
    return nums[0] + recursive_sum(*nums[1:])

# task B
def recursive_digit_sum(num):
    while num >= 10:
        return num % 10 + recursive_digit_sum(num // 10)
    return num

# task C
def make_equation(*num):
    if len(num) == 1:
        return f'{num[0]}'
    else:
        return f'({make_equation(*num[:-1])}) * x + {num[-1]}'

# task D
def answer(func):
    def code(*args, **kwargs):
        return f'Результат функции: {func(*args, **kwargs)}'
    return code

# task E
def result_accumulator(func):
    queue = []

    def wrapper(*args, method='accumulate', **kwargs):
        if method == 'accumulate':
            queue.append(func(*args, **kwargs))
        elif method == 'drop':
            queue.append(func(*args, **kwargs))
            result = queue[:]
            queue.clear()
            return result
    return wrapper

# task F
def merge(left, right):
    result = []
    pos_left = pos_right = 0

    while pos_left < len(left) and pos_right < len(right):
        if left[pos_left] < right[pos_right]:
            result.append(left[pos_left])
            pos_left += 1
        else:
            result.append(right[pos_right])
            pos_right += 1

    result += left[pos_left:]
    result += right[pos_right:]

    return result


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

# task G
def same_type(func):
    def wrapper(*args):
        if len({type(item) for item in args}) != 1:
            print("Обнаружены различные типы данных")
            return False
        return func(*args)
    return wrapper

# task H
def fibonacci(num):
    a = 0
    b = 1
    for _ in range(num):
        yield a
        a, b = b, a + b

# task I
def cycle(iterable):
    while True:
        for item in iterable:
            yield item

# task J
def make_linear(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(make_linear(item))
        else:
            result.append(item)
    return result

