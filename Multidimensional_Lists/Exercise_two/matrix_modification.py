rows = int(input())

matrix = []

for i in range (rows):

    matrix.append([int(x) for x in input().split()])

while True:

    command = input()

    if command == "END":
        break

    command_args = command.split()

    row = int(command_args[1])

    col = int(command_args[2])

    value = int(command_args[3])

    if row < 0 or row >= rows or col < 0 or col >= rows:


        print("Invalid coordinates")
        continue

    command_type = command_args[0]

    if command_type == "Add":

        matrix[row][col] += value

    elif command_type == "Subtract":

        matrix[row][col] -= value

for i in matrix:

    print(" ".join([str(x) for x in i]))