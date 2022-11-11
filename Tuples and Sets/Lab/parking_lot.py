number_of_cars = int(input())

parking_lot = []

for car in range(number_of_cars):

    direction, car_number = input().split(", ")

    if direction == "IN" and car_number not in parking_lot:

        parking_lot.append(car_number)

    elif direction == "OUT" and car_number in parking_lot:

        parking_lot.remove(car_number)


if parking_lot:

    for car in parking_lot:
        print(car)

else:
    print("Parking Lot is Empty")