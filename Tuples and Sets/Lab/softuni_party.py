number_of_guests = int(input())

missing_guests = []

for guest in range(number_of_guests):

    reservation_number = input()

    if reservation_number not in missing_guests:

        missing_guests.append(reservation_number)

while True:

    command = input()

    if command == "END":
        break

    else:
        arrived_guest = command

        if arrived_guest in missing_guests:

            missing_guests.remove(arrived_guest)

print(len(missing_guests))

for guest in sorted(missing_guests):
    print(guest)