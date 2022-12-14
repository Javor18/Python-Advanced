from collections import deque

chocolates = [int(x) for x in input().split(", ")]

cups_of_milk = deque([int(x) for x in input().split(", ")])

milkshakes = 0

while chocolates and cups_of_milk and milkshakes < 5:

    chocolate = chocolates.pop()

    milk_cup = cups_of_milk.popleft()

    if chocolate <= 0 and milk_cup <= 0:
        continue

    if chocolate <= 0:
        cups_of_milk.appendleft(milk_cup)
        continue

    if milk_cup <= 0:

        chocolates.append(chocolate)
        continue

    if chocolate == milk_cup:

        milkshakes += 1

    else:
        chocolates.append(chocolate - 5)
        cups_of_milk.append(milk_cup)

if milkshakes == 5:

    print("Great! You made all the chocolate milkshakes needed!")

else:

    print("Not enough milkshakes.")

if chocolates:

    print(f"Chocolate: {', '.join([str(x) for x in chocolates])}")

else:
    print("Chocolate: empty")

if cups_of_milk:

    print(f"Milk: {', '.join([str(x) for x in cups_of_milk])}")

else:
    print("Milk: empty")