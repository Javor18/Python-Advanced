from collections import deque

milligrams_of_caffeinе = deque(int(x) for x in input().split(", "))
energy_drinks = deque(int(x) for x in input().split(", "))

max_caffeinе = 300

stamats_caffeine = 0

while milligrams_of_caffeinе and energy_drinks:

    milligrams = milligrams_of_caffeinе.pop()
    energy_drink = energy_drinks.popleft()

    caffeine = milligrams * energy_drink

    if caffeine + stamats_caffeine <= max_caffeinе:
        stamats_caffeine += caffeine

    else:
        energy_drinks.append(energy_drink)
        stamats_caffeine -= 30

        if stamats_caffeine < 0:
            stamats_caffeine = 0

if energy_drinks:

    print(f"Drinks left: {', '.join(str(x) for x in energy_drinks)}")

else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")

print(f"Stamat is going to sleep with {stamats_caffeine} mg caffeine.")