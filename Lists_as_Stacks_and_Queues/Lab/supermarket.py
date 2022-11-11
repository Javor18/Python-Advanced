
people = []

while True:
    command = input()

    if command == 'End':
        break

    elif command == 'Paid':
        print('\n'.join(people))
        people.clear()

    else:
        people.append(command)

print(f'{len(people)} people remaining.')