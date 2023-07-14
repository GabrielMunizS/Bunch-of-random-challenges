# this
squares = []
for num in range(1, 6):
    squares.append(num ** 2)

print(squares)

#is the same as

squares = [num ** 2 for num in range(1, 6)]

print(squares)
