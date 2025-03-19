# task A
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


class PatchedPoint(Point):
    def __init__(self, *args) -> None:
        match len(args):
            case 0:
                super().__init__(0, 0)
            case 1:
                super().__init__(*args[0])
            case 2:
                super().__init__(*args)

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


class PatchedPoint(Point):
    def __init__(self, *args) -> None:
        match len(args):
            case 0:
                self.x = 0
                self.y = 0
            case 1:
                self.x, self.y = args[0]
            case 2:
                self.x, self.y = args

    def __str__(self) -> str:
        string = f'({self.x}, {self.y})'
        return string

    def __repr__(self) -> str:
        string = f'PatchedPoint({self.x}, {self.y})'
        return string

# task C
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


class PatchedPoint(Point):
    def __init__(self, *args) -> None:
        match len(args):
            case 0:
                self.x = 0
                self.y = 0
            case 1:
                self.x, self.y = args[0]
            case 2:
                self.x, self.y = args

    def __add__(self, other):
        return PatchedPoint(self.x + other[0], self.y + other[1])

    def __iadd__(self, other):
        self.move(other[0], other[1])
        return self

    def __str__(self) -> str:
        string = f'({self.x}, {self.y})'
        return string

    def __repr__(self) -> str:
        string = f'PatchedPoint({self.x}, {self.y})'
        return string

# task D
class Fraction():
    def __init__(self, *args) -> None:
        if isinstance(args[0], str):
            self.__num, self.__den = [int(c) for c in args[0].split('/')]
        else:
            self.__num = args[0]
            self.__den = args[1]
        self.__reduction()

    def __gcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return abs(a)

    def __reduction(self):
        gcd = self.__gcd(self.__num, self.__den)
        self.__num = self.__num // gcd
        self.__den = self.__den // gcd
        return self

    def __str__(self) -> str:
        return f'{self.__num}/{self.__den}'

    def __repr__(self) -> str:
        return f"Fraction({self.__num}, {self.__den})"

    def numerator(self, *args):
        if len(args):
            self.__num = args[0]
            self.__reduction()
        return self.__num

    def denominator(self, *args):
        if len(args):
            self.__den = args[0]
            self.__reduction()
        return self.__den

# task E
class Fraction():
    def __init__(self, *args) -> None:
        if isinstance(args[0], str):
            self.__num, self.__den = [int(c) for c in args[0].split('/')]
        else:
            self.__num = args[0]
            self.__den = args[1]
        self.__reduction()

    def __sign(self):
        return -1 if self.__num < 0 else 1

    def __neg__(self) -> 'Fraction':
        return Fraction(-self.__num, self.__den)

    def __gcd(self, a, b) -> int:
        while b:
            a, b = b, a % b
        return abs(a)

    def __reduction(self) -> 'Fraction':
        __gcd = self.__gcd(self.__num, self.__den)
        self.__num //= __gcd
        self.__den //= __gcd

        if self.__den < 0:
            self.__num = -self.__num
            self.__den = abs(self.__den)
        return self

    def __str__(self) -> str:
        return f'{self.__num}/{self.__den}'

    def __repr__(self) -> str:
        return f"Fraction('{self.__num}/{self.__den}')"

    def numerator(self, *args) -> int:
        if len(args):
            self.__num = args[0] * self.__sign()
            self.__reduction()
        return abs(self.__num)

    def denominator(self, *args) -> int:
        if len(args):
            self.__den = args[0]
        self.__reduction()
        return abs(self.__den)

# task F
class Fraction():
    def __init__(self, *args) -> None:
        if isinstance(args[0], str):
            self.__num, self.__den = [int(c) for c in args[0].split('/')]
        else:
            self.__num = args[0]
            self.__den = args[1]
        self.__reduction()

    def __sign(self):
        return -1 if self.__num < 0 else 1

    def __neg__(self) -> 'Fraction':
        return Fraction(-self.__num, self.__den)

    def __add__(self, other) -> 'Fraction':
        denominator = self.denominator() * other.denominator()
        numerator = self.__num * other.__den + other.__num * self.__den
        return Fraction(numerator, denominator)

    def __sub__(self, other) -> 'Fraction':
        denominator = self.denominator() * other.denominator()
        numerator = self.__num * other.__den - other.__num * self.__den
        return Fraction(numerator, denominator)

    def __iadd__(self, other) -> 'Fraction':
        common_denominator = self.denominator() * other.denominator()
        self.__num = self.__num * other.__den + other.__num * self.__den
        self.__den = common_denominator
        self.__reduction()
        return self

    def __isub__(self, other) -> 'Fraction':
        common_denominator = self.denominator() * other.denominator()
        self.__num = self.__num * other.__den - other.__num * self.__den
        self.__den = common_denominator
        self.__reduction()
        return self

    def __gcd(self, a, b) -> int:
        while b:
            a, b = b, a % b
        return abs(a)

    def __reduction(self) -> tuple:
        __gcd = self.__gcd(self.__num, self.__den)
        self.__num //= __gcd
        self.__den //= __gcd

        if self.__den < 0:
            self.__num = -self.__num
            self.__den = abs(self.__den)
        return self.__num, self.__den

    def __str__(self) -> str:
        return f'{self.__num}/{self.__den}'

    def __repr__(self) -> str:
        return f"Fraction('{self.__num}/{self.__den}')"

    def numerator(self, *args) -> int:
        if len(args):
            self.__num = args[0] * self.__sign()
            self.__reduction()
        return abs(self.__num)

    def denominator(self, *args) -> int:
        if len(args):
            self.__den = args[0]
        self.__reduction()
        return abs(self.__den)

# task G
class Fraction():
    def __init__(self, *args) -> None:
        if isinstance(args[0], str):
            self.__num, self.__den = [int(c) for c in args[0].split('/')]
        else:
            self.__num = args[0]
            self.__den = args[1]
        self.__reduction()

    def __sign(self):
        return -1 if self.__num < 0 else 1

    def __neg__(self) -> 'Fraction':
        return Fraction(-self.__num, self.__den)

    def __add__(self, other) -> 'Fraction':
        common_denominator = self.__den * other.__den
        new = Fraction(1, 1)
        new.__num = self.__num * other.__den + other.__num * self.__den
        new.__den = common_denominator
        new.__reduction()
        return new

    def __sub__(self, other) -> 'Fraction':
        common_denominator = self.__den * other.__den
        new = Fraction(1, 1)
        new.__num = self.__num * other.__den - other.__num * self.__den
        new.__den = common_denominator
        new.__reduction()
        return new

    def __iadd__(self, other) -> 'Fraction':
        common_denominator = self.__den * other.__den
        self.__num = self.__num * other.__den + other.__num * self.__den
        self.__den = common_denominator
        self.__reduction()
        return self

    def __isub__(self, other) -> 'Fraction':
        common_denominator = self.__den * other.__den
        self.__num = self.__num * other.__den - other.__num * self.__den
        self.__den = common_denominator
        self.__reduction()
        return self

    def __mul__(self, other) -> 'Fraction':
        common_denominator = self.__den * other.__den
        new = Fraction(1, 1)
        new.__num = self.__num * other.__num
        new.__den = common_denominator
        new.__reduction()
        return new

    def __truediv__(self, other) -> 'Fraction':
        new = Fraction(self.__num, self.__den)
        new.__reduction()
        return new.__mul__(other.reverse())

    def __imul__(self, other) -> 'Fraction':
        common_denominator = self.__den * other.__den
        self.__num = self.__num * other.__num
        self.__den = common_denominator
        self.__reduction()
        return self

    def __itruediv__(self, other) -> 'Fraction':
        return self.__imul__(other.reverse())

    def _gcd(self, a, b) -> int:
        while b:
            a, b = b, a % b
        return abs(a)

    def __reduction(self) -> tuple:
        __gcd = self._gcd(self.__num, self.__den)
        self.__num //= __gcd
        self.__den //= __gcd

        if self.__den < 0:
            self.__num = -self.__num
            self.__den = abs(self.__den)
        return self.__num, self.__den

    def __str__(self) -> str:
        return f'{self.__num}/{self.__den}'

    def __repr__(self) -> str:
        return f"Fraction('{self.__num}/{self.__den}')"

    def numerator(self, *args) -> int:
        if len(args):
            self.__num = args[0] * self.__sign()
            self.__reduction()
        return abs(self.__num)

    def denominator(self, *args) -> int:
        if len(args):
            self.__den = args[0]
        self.__reduction()
        return abs(self.__den)

    def reverse(self) -> 'Fraction':
        return Fraction(self.__den, self.__num)

# task H
class Fraction():
    def __init__(self, *args) -> None:
        if isinstance(args[0], str):
            self.__num, self.__den = [int(c) for c in args[0].split('/')]
        else:
            self.__num = args[0]
            self.__den = args[1]
        self.__reduction()

    def __neg__(self) -> 'Fraction':
        return Fraction(-self.__num, self.__den)

    def __add__(self, other) -> 'Fraction':
        denominator = self.denominator() * other.denominator()
        numerator = self.__num * other.__den + other.__num * self.__den
        return Fraction(numerator, denominator)

    def __sub__(self, other) -> 'Fraction':
        denominator = self.denominator() * other.denominator()
        numerator = self.__num * other.__den - other.__num * self.__den
        return Fraction(numerator, denominator)

    def __iadd__(self, other) -> 'Fraction':
        self.__num = self.__num * other.__den + other.__num * self.__den
        self.__den = self.__den * other.__den
        self.__reduction()
        return self

    def __isub__(self, other) -> 'Fraction':
        self.__num = self.__num * other.__den - other.__num * self.__den
        self.__den = self.__den * other.__den
        self.__reduction()
        return self

    def __mul__(self, other) -> 'Fraction':
        denominator = self.__den * other.__den
        numerator = self.__num * other.__num
        return Fraction(numerator, denominator)

    def __truediv__(self, other) -> 'Fraction':
        new = Fraction(self.__num, self.__den)
        return new.__mul__(other.reverse())

    def __imul__(self, other) -> 'Fraction':
        self.__num = self.__num * other.__num
        self.__den = self.__den * other.__den
        self.__reduction()
        return self

    def __itruediv__(self, other) -> 'Fraction':
        return self.__imul__(other.reverse())

    def __gt__(self, other) -> bool:
        return self.__num * other.__den > other.__num * self.__den

    def __lt__(self, other) -> bool:
        return self.__num * other.__den < other.__num * self.__den

    def __ge__(self, other) -> bool:
        return self.__num * other.__den >= other.__num * self.__den

    def __le__(self, other) -> bool:
        return self.__num * other.__den <= other.__num * self.__den

    def __eq__(self, other) -> bool:
        return self.__num * other.__den == other.__num * self.__den

    def __ne__(self, other) -> bool:
        return self.__num * other.__den != other.__num * self.__den

    def __str__(self) -> str:
        return f'{self.__num}/{self.__den}'

    def __repr__(self) -> str:
        return f"Fraction('{self.__num}/{self.__den}')"

    def numerator(self, *args) -> int:
        if len(args):
            self.__num = args[0] * self.__sign()
            self.__reduction()
        return abs(self.__num)

    def __sign(self):
        return -1 if self.__num < 0 else 1

    def __gcd(self, a, b) -> int:
        while b:
            a, b = b, a % b
        return abs(a)

    def __reduction(self) -> tuple:
        __gcd = self.__gcd(self.__num, self.__den)
        self.__num //= __gcd
        self.__den //= __gcd

        if self.__den < 0:
            self.__num = -self.__num
            self.__den = abs(self.__den)
        return self.__num, self.__den

    def denominator(self, *args) -> int:
        if len(args):
            self.__den = args[0]
        self.__reduction()
        return abs(self.__den)

    def reverse(self) -> 'Fraction':
        return Fraction(self.__den, self.__num)

# task I
class Fraction():

    def __init__(self, *args) -> None:

        self.__den = 1

        if isinstance(args[0], str):

            splits = args[0].split('/')

            if len(splits) == 1:

                self.__num = int(args[0])

            else:

                self.__num, self.__den = [int(c) for c in splits]

        elif len(args) == 1 and isinstance(args[0], int):

            self.__num = args[0]

        else:

            self.__num = args[0]

            self.__den = args[1]

        self.__reduction()

    def __neg__(self) -> 'Fraction':

        return Fraction(-self.__num, self.__den)

    def _check_other(self, other):

        if isinstance(other, int):
            return Fraction(other, 1)

        return other

    def __add__(self, other) -> 'Fraction':

        other = self._check_other(other)

        denominator = self.denominator() * other.denominator()

        numerator = self.__num * other.__den + other.__num * self.__den

        return Fraction(numerator, denominator)

    def __sub__(self, other) -> 'Fraction':

        other = self._check_other(other)

        denominator = self.denominator() * other.denominator()

        numerator = self.__num * other.__den - other.__num * self.__den

        return Fraction(numerator, denominator)

    def __iadd__(self, other) -> 'Fraction':

        other = self._check_other(other)

        self.__num = self.__num * other.__den + other.__num * self.__den

        self.__den = self.__den * other.__den

        self.__reduction()

        return self

    def __isub__(self, other) -> 'Fraction':

        other = self._check_other(other)

        self.__num = self.__num * other.__den - other.__num * self.__den

        self.__den = self.__den * other.__den

        self.__reduction()

        return self

    def __mul__(self, other) -> 'Fraction':

        denominator = self.__den * other.__den

        numerator = self.__num * other.__num

        return Fraction(numerator, denominator)

    def __truediv__(self, other) -> 'Fraction':

        new = Fraction(self.__num, self.__den)

        return new.__mul__(other.reverse())

    def __imul__(self, other) -> 'Fraction':

        self.__num = self.__num * other.__num

        self.__den = self.__den * other.__den

        self.__reduction()

        return self

    def __itruediv__(self, other) -> 'Fraction':

        other = self._check_other(other)

        return self.__imul__(other.reverse())

    def __gt__(self, other) -> bool:

        other = self._check_other(other)

        return self.__num * other.__den > other.__num * self.__den

    def __lt__(self, other) -> bool:

        other = self._check_other(other)

        return self.__num * other.__den < other.__num * self.__den

    def __ge__(self, other) -> bool:

        other = self._check_other(other)

        return self.__num * other.__den >= other.__num * self.__den

    def __le__(self, other) -> bool:

        other = self._check_other(other)

        return self.__num * other.__den <= other.__num * self.__den

    def __eq__(self, other) -> bool:

        other = self._check_other(other)

        return self.__num * other.__den == other.__num * self.__den

    def __ne__(self, other) -> bool:

        other = self._check_other(other)

        return self.__num * other.__den != other.__num * self.__den

    def __str__(self) -> str:

        return f'{self.__num}/{self.__den}'

    def __repr__(self) -> str:

        return f"Fraction('{self.__num}/{self.__den}')"

    def numerator(self, *args) -> int:

        if len(args):
            self.__num = args[0] * self.__sign()

            self.__reduction()

        return abs(self.__num)

    def __sign(self):

        return -1 if self.__num < 0 else 1

    def __gcd(self, a, b) -> int:

        while b:
            a, b = b, a % b

        return abs(a)

    def __reduction(self) -> tuple:

        gcd = self.__gcd(self.__num, self.__den)

        self.__num //= gcd

        self.__den //= gcd

        if self.__den < 0:
            self.__num = -self.__num

            self.__den = abs(self.__den)

        return self.__num, self.__den

    def denominator(self, *args) -> int:

        if len(args):
            self.__den = args[0]

        self.__reduction()

        return abs(self.__den)

    def reverse(self) -> 'Fraction':

        return Fraction(self.__den, self.__num)

# task J
class Fraction():
    def __init__(self, *args) -> None:
        self.__den = 1
        if isinstance(args[0], str):
            splits = args[0].split('/')
            if len(splits) == 1:
                self.__num = int(args[0])
            else:
                self.__num, self.__den = [int(c) for c in splits]
        elif len(args) == 1 and isinstance(args[0], int):
            self.__num = args[0]
        else:
            self.__num = args[0]
            self.__den = args[1]
        self.__reduction()

    def __neg__(self) -> 'Fraction':
        return Fraction(-self.__num, self.__den)

    def __check_other(self, other):
        if isinstance(other, int):
            return Fraction(other, 1)
        return other

    def __add__(self, other) -> 'Fraction':
        other = self.__check_other(other)
        denominator = self.denominator() * other.denominator()
        numerator = self.__num * other.__den + other.__num * self.__den
        return Fraction(numerator, denominator)

    def __radd__(self, other) -> 'Fraction':
        return self.__add__(other)

    def __iadd__(self, other) -> 'Fraction':
        other = self.__check_other(other)
        self.__num = self.__num * other.__den + other.__num * self.__den
        self.__den = self.__den * other.__den
        self.__reduction()
        return self

    def __sub__(self, other) -> 'Fraction':
        other = self.__check_other(other)
        denominator = self.denominator() * other.denominator()
        numerator = self.__num * other.__den - other.__num * self.__den
        return Fraction(numerator, denominator)

    def __rsub__(self, other) -> 'Fraction':
        return -self.__sub__(other)

    def __isub__(self, other) -> 'Fraction':
        other = self.__check_other(other)
        self.__num = self.__num * other.__den - other.__num * self.__den
        self.__den = self.__den * other.__den
        self.__reduction()
        return self

    def __mul__(self, other) -> 'Fraction':
        other = self.__check_other(other)
        denominator = self.__den * other.__den
        numerator = self.__num * other.__num
        return Fraction(numerator, denominator)

    def __rmul__(self, other) -> 'Fraction':
        return self.__mul__(other)

    def __imul__(self, other) -> 'Fraction':
        other = self.__check_other(other)
        self.__num = self.__num * other.__num
        self.__den = self.__den * other.__den
        self.__reduction()
        return self

    def __truediv__(self, other) -> 'Fraction':
        other = self.__check_other(other)
        new = Fraction(self.__num, self.__den)
        return new.__mul__(other.reverse())

    def __rtruediv__(self, other) -> 'Fraction':
        return self.__truediv__(other).reverse()

    def __itruediv__(self, other) -> 'Fraction':
        other = self.__check_other(other)
        return self.__imul__(other.reverse())

    def __gt__(self, other) -> bool:
        other = self.__check_other(other)
        return self.__num * other.__den > other.__num * self.__den

    def __rgt__(self, other) -> bool:
        return self.__gt__(other)

    def __lt__(self, other) -> bool:
        other = self.__check_other(other)
        return self.__num * other.__den < other.__num * self.__den

    def __rlt__(self, other) -> bool:
        return self.__lt__(other)

    def __ge__(self, other) -> bool:
        other = self.__check_other(other)
        return self.__num * other.__den >= other.__num * self.__den

    def __rge__(self, other) -> bool:
        return self.__ge__(other)

    def __le__(self, other) -> bool:
        other = self.__check_other(other)
        return self.__num * other.__den <= other.__num * self.__den

    def __rle__(self, other) -> bool:
        return self.__le__(other)

    def __eq__(self, other) -> bool:
        other = self.__check_other(other)
        return self.__num * other.__den == other.__num * self.__den

    def __req__(self, other) -> bool:
        return self.__eq__(other)

    def __ne__(self, other) -> bool:
        other = self.__check_other(other)
        return self.__num * other.__den != other.__num * self.__den

    def __rne__(self, other) -> bool:
        return self.__ne__(other)

    def __str__(self) -> str:
        return f'{self.__num}/{self.__den}'

    def __repr__(self) -> str:
        return f"Fraction('{self.__num}/{self.__den}')"

    def numerator(self, *args) -> int:
        if len(args):
            self.__num = args[0] * self.__sign()
            self.__reduction()
        return abs(self.__num)

    def __sign(self):
        return -1 if self.__num < 0 else 1

    def __gcd(self, a, b) -> int:
        while b:
            a, b = b, a % b
        return abs(a)

    def __reduction(self) -> tuple:
        gcd = self.__gcd(self.__num, self.__den)
        self.__num //= gcd
        self.__den //= gcd

        if self.__den < 0:
            self.__num = -self.__num
            self.__den = abs(self.__den)
        return self.__num, self.__den

    def denominator(self, *args) -> int:
        if len(args):
            self.__den = args[0]
        self.__reduction()
        return abs(self.__den)

    def reverse(self) -> 'Fraction':
        return Fraction(self.__den, self.__num)


