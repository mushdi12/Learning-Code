# task A
[number ** 2 for number in range(a, b + 1)]

# task B
[[(i + 1) * (j + 1) for j in range(n)] for i in range(n)]

# task C
[len(word) for word in sentence.split()]

# task D
{num for num in numbers if num % 2 == 1}

# task E
{num for num in numbers if int(num ** (0.5)) ** 2 == num}

# task F
{letter: text.lower().count(letter) for letter in set(text.lower()) if letter.isalpha()}

# task G
{number: [divider for divider in range(1, number + 1) if number % divider == 0] for number in numbers}

# task H
''.join(word[0].upper() for word in string.split())

# task I
' - '.join([str(num) for num in sorted(set(numbers))])

# task J
''.join(char * count for char, count in rle)
