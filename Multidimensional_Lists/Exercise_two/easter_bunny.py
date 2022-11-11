size = int(input())

matrix = []

bunny_pos = []
bunny_path = []

best_direction = None
max_collected_eggs = 0

directions = {

    'up': (-1, 0),
    'down': (1, 0),
    'right': (0, 1),
    'left': (0, -1)
}
for row in range (size):

    command = input().split()

    if 'B' in command:

        bunny_pos = [row, command.index('B')]

    matrix.append(command)

for direction, position in directions.items():

    row, col = [

        bunny_pos[0] + position[0],
        bunny_pos[1] + position[1]
    ]

    path = []

    collected_eggs = 0

    while 0 <= row < size and 0 <= col < size:

        if matrix[row][col] == 'X':
            break

        collected_eggs += int(matrix[row][col])
        path.append([row, col])

        row += position[0]
        col += position[1]

        if collected_eggs >= max_collected_eggs:

            max_collected_eggs = collected_eggs
            best_direction = direction
            bunny_path = path

print(best_direction)

print(*bunny_path, sep='\n')

print(max_collected_eggs)