directions = {"up": [-1, 0],
              "down": [1, 0],
              "left": [0, -1],
              "right": [0, 1]}

matrix_size = int(input())

food_quantity = 0

matrix = []

lairs = []

for row in range(matrix_size):
    matrix.append(list(input()))
    if "S" in matrix[row]:
        snake_row, snake_col = row, matrix[row].index("S")
    elif "B" in matrix[row]:
        lairs.append([row, matrix[row].index("B")])

while food_quantity < 10:

    direction = input()
    matrix[snake_row][snake_col] = '.'

    snake_row += directions[direction][0]
    snake_col += directions[direction][1]

    if 0 <= snake_row >= matrix_size or 0 <= snake_col >= matrix_size:

        print("Game over!")
        break

    position = matrix[snake_row][snake_col]

    if position == "*":

        food_quantity += 1

    elif position == "B":

        if len(lairs) > 1:

            i, x = lairs[0]
            matrix[i][x] = '.'

            burrow = lairs[1]
            snake_row = burrow[0]
            snake_col = burrow[1]

            lairs = []

    matrix[snake_row][snake_col] = 'S'
if food_quantity == 10:

    print("You won! You fed the snake.")

print(f"Food eaten: {food_quantity}")

for line in matrix:

    print(''.join(x for x in line))