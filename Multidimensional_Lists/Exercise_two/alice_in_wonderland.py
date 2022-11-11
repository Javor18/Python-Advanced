
#square shape
size = int(input())

alice_pos = []

collected_tea = 0

matrix = []

directions = {

    'up': (-1, 0),
    'down': (1, 0),
    'right': (0, 1),
    'left': (0, -1)
}

for row in range (size):

    command = input().split()

    matrix.append(command)

    if "A" in command:

        alice_pos = [row, command.index("A")]

        matrix[row][alice_pos[1]] = "*"

while collected_tea < 10:

    direction = input()

    row = alice_pos[0] + directions[direction][0]
    col = alice_pos[1] + directions[direction][1]

    if not (0 <= row < size and 0 <= col < size):
        break

    alice_pos = [row, col]

    position = matrix[row][col]

    matrix[row][col] = "*"

    if position == "R":
        break

    if position.isdigit():

        collected_tea += int(position)

if collected_tea < 10:

    print("Alice didn't make it to the tea party.")

else:
    print("She did it! She went to the party.")

print(*[' '.join(x) for x in matrix], sep="\n")