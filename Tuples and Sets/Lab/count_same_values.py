numbers = tuple(map(float, input().split()))

unique_numbers = []

for number in numbers:

    if number not in unique_numbers:
        unique_numbers.append(number)

for number in unique_numbers:

    number_count = numbers.count(number)
    print(f"{number} - {number_count} times")