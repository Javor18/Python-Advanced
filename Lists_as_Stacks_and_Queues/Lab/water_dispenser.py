from collections import deque

quantity_of_water = int(input())

command = input()

queue = deque()

while command != "Start":

    name = command

    queue.append(name)

    command = input()

while True:
    command = input()

    if command == "End":
        break

    else:
        command = command.split()

        if len(command) == 2:

            type_of_command, water = [int(x) if x.isdigit() else x for x in command]

            if type_of_command == "refill":

                quantity_of_water += water

        else:
            need_water = int(command[0])

            person_name = queue.popleft()

            if quantity_of_water >= need_water:
                print(f"{person_name} got water")
                quantity_of_water -= need_water

            else:
                print(f"{person_name} must wait")

print(f"{quantity_of_water} liters left")
