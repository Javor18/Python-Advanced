def move(direction, steps):

    r = my_position[0] + (directions[direction][0] * steps)
    c = my_position[1] + (directions[direction][1] * steps)

    if not (0 <= r < size and 0 <= c < size):

        return my_position

    if shotgun_range[r][c] == "x":

        return my_position

    return [r, c]

def shoot(direction):
    r = my_position[0] + directions[direction][0]
    c = my_position[1] + directions[direction][1]

    while 0 <= r < size and 0 <= c < size:

        if shotgun_range[r][c] == "x":

            shotgun_range[r][c] = "."

            return [r, c]

        r += directions[direction][0]
        c += directions[direction][1]


size = 5

targets = 0
targets_hit = 0
targets_hit_position = []

my_position = []
target = []

shotgun_range = []

directions = {

    'up': (-1, 0),
    'down': (1, 0),
    'right': (0, 1),
    'left': (0, -1)
}

for row in range (size):

    command = input().split()

    shotgun_range.append(command)

    if "A" in command:

        my_position = [row, command.index("A")]

        shotgun_range[row][my_position[1]] = "."

    targets += command.count("x")

number_of_commands = int(input())

for _ in range(number_of_commands):

    string = input().split()

    command_type = string[0]

    if command_type == "move":

        my_position = move(string[1], int(string[2]))

    elif command_type == "shoot":

        target_down = shoot(string[1])

        if target_down:

            targets_hit_position.append(target_down)

            targets_hit += 1

        if targets_hit == targets:

            print(f"Training completed! All {targets_hit} targets hit.")
            break

if targets_hit < targets:

    print(f"Training not completed! {targets - targets_hit} targets left.")

[print(target_position) for target_position in targets_hit_position]