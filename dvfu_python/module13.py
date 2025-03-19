# task A
class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

# task B
class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def move(self, new_x, new_y):
        self.x += new_x
        self.y += new_y

    def length(self, point):
        result = ((point.x - self.x) ** 2 + (point.y - self.y) ** 2) ** 0.5
        return round(result, 2)

# task C
class RedButton:
    def __init__(self) -> None:
        self.counter = 0

    def click(self):
        self.counter += 1
        print('Тревога!')

    def count(self):
        return self.counter

# task D
class Programmer:
    __rank = {
        'Junior': 10,
        'Middle': 15,
        'Senior': 20,
    }

    def __init__(self, name, position):
        self.name = name
        self.position = position
        self.bonus = 0
        self.work_time = 0
        self.salary = 0

    def work(self, time):
        self.work_time += time
        self.salary += (self.__rank[self.position] + self.bonus) * time

    def info(self):
        return f'{self.name} {self.work_time}ч. {self.salary}тгр.'

    def rise(self):
        match self.position:
            case 'Junior':
                self.position = 'Middle'
            case 'Middle':
                self.position = 'Senior'
            case 'Senior':
                self.bonus += 1

# task E
class Rectangle:
    def __init__(self, corner1, corner2) -> None:
        self.left_down = min(corner1[0], corner2[0]), min(corner1[1], corner2[1])
        self.up_right = max(corner1[0], corner2[0]), max(corner1[1], corner2[1])

    def perimeter(self):
        return round((self.up_right[0] - self.left_down[0]) * 2 +
                     (self.up_right[1] - self.left_down[1]) * 2, 2)

    def area(self):
        return round((self.up_right[0] - self.left_down[0]) *
                     (self.up_right[1] - self.left_down[1]), 2)

# task F
class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.round()

    def round(self):
        self.x = round(self.x, 2)
        self.y = round(self.y, 2)
        return self


class Rectangle:
    def __init__(self, corner1, corner2) -> None:
        self.corner = Point(min(corner1[0], corner2[0]), max(corner1[1], corner2[1]))  # noqa
        self.width = round(max(corner1[0], corner2[0]) - self.corner.x, 2)
        self.height = round(self.corner.y - min(corner1[1], corner2[1]), 2)

    def perimeter(self):
        return round((self.width + self.height) * 2, 2)

    def area(self):
        return round(self.width * self.height, 2)

    def get_pos(self):
        return self.corner.x, self.corner.y

    def get_size(self):
        return self.width, self.height

    def move(self, dx, dy):
        self.corner.x += dx
        self.corner.y += dy
        self.corner.round()

    def resize(self, width, height):
        self.width = round(width, 2)
        self.height = round(height, 2)

# task G
class Point:
    def __init__(self, x, y):
        self.x = round(x, 2)
        self.y = round(y, 2)
        self.round()

    def round(self):
        self.x = round(self.x, 2)
        self.y = round(self.y, 2)
        return self


class Rectangle(Point):
    def __init__(self, corner1, corner2):
        self.x = min(corner1[0], corner2[0])
        self.y = max(corner1[1], corner2[1])
        self.width = round(max(corner1[0], corner2[0]) - self.x, 2)
        self.height = round(self.y - min(corner1[1], corner2[1]), 2)

    def perimeter(self):
        return round((self.width + self.height) * 2, 2)

    def area(self):
        return round(self.width * self.height, 2)

    def get_pos(self):
        return self.x, self.y

    def get_size(self):
        return self.width, self.height

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        self.round()

    def resize(self, width, height):
        self.width = round(width, 2)
        self.height = round(height, 2)

    def turn(self):
        delta = round((self.width - self.height) / 2, 2)
        self.move(delta, delta)
        self.height, self.width = self.width, self.height

    def scale(self, ratio):
        dx = round((self.width * (ratio - 1)), 2)
        dy = round((self.height * (ratio - 1)), 2)
        self.move(-dx / 2, dy / 2)
        self.resize(self.width * ratio, self.height * ratio)

# task H
class Cell():
    def __init__(self, cell_item='X') -> None:
        self.state = cell_item

    def status(self):
        return self.state

    def remove_check(self):
        check = self.status()
        self.state = 'X'
        return check

    def set_check(self, check):
        old_check = self.status()
        self.state = check
        return old_check


class Checkers():
    def __init__(self) -> None:
        self.cells = dict()
        checker_board = 'XBXBXBXB' + 'BXBXBXBX' + 'XBXBXBXB' + 'XXXXXXXX' + \
            'XXXXXXXX' + 'WXWXWXWX' + 'XWXWXWXW' + 'WXWXWXWX'

        i = 0
        for row in '87654321':
            for col in 'ABCDEFGH':
                self.cells[col + row] = Cell(cell_item=checker_board[i])
                i += 1

    def get_cell(self, cell):
        return self.cells[cell]

    def move(self, where_from, where_to):
        check = self.cells[where_from].remove_check()
        return self.cells[where_to].set_check(check)

# task I
class Node:
    def __init__(self, item) -> None:
        self.item = item
        self.next = None


class Queue:
    def __init__(self) -> None:
        self.head = self.tail = None

    def push(self, item):
        new_node = Node(item)
        if self.is_empty():
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node
            self.tail = new_node

    def pop(self):
        if self.is_empty():
            return None
        temp = self.head.item
        self.head = self.head.next
        return temp

    def is_empty(self):
        return self.head is None

# task J
class Node:
    def __init__(self, item) -> None:
        self.item = item
        self.next = None


class Stack:
    def __init__(self) -> None:
        self.head = None

    def push(self, item):
        if self.is_empty():
            self.head = Node(item)
        else:
            new_node = Node(item)
            new_node.next = self.head
            self.head = new_node

    def pop(self):
        if self.is_empty():
            return None
        item = self.head.item
        self.head = self.head.next
        return item

    def is_empty(self):
        return self.head is None


