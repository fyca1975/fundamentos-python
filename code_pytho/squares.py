numbers = [1, 2, 3, 4, 5]

# poco eficiente
squares = []
for number in numbers:
    squares.append(number ** 2)
print(squares)

# más eficiente
squares_v2 = [number ** 2 for number in numbers]
print(squares_v2)
