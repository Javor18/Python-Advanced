matrix_size = int(input())

racing_number = input()

row, col = 0, 0

matrix = []

for x in range(matrix_size):

    matrix.append(input().split())

    if "T" in matrix[x]:

        t_row, t_col = x, matrix[x].index("T")


directions = {"up": [-1, 0],
             "down": [1, 0],
             "left": [0, -1],
             "right": [0, 1]}

distance = 0

while True:

    direction = input()

    if direction == "End":
        matrix[row][col] = "C"
        print(f"Racing car {racing_number} DNF.")
        break

    row += directions[direction][0]
    col += directions[direction][1]

    position = matrix[row][col]
    matrix[row][col] = "C"

    if position == ".":

        distance += 10

    elif position == "T":

        matrix[row][col] = "."
        row = t_row
        col = t_col

        distance += 30
        matrix[row][col] = "."

    elif position == "F":

        print(f"Racing car {racing_number} finished the stage!")
        distance += 10
        break

    matrix[row][col] = "."

print(f"Distance covered {distance} km.")

for line in matrix:

    print(''.join(str(x) for x in line))