numbers = input().split()

reversed_numbers = []

while len(numbers) > 0:

    reversed_numbers.append(numbers.pop())

print(" ".join(reversed_numbers))