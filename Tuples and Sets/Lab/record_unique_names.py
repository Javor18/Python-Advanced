number_of_names = int(input())

unique_names = []

for i in range(number_of_names):

    name = input()

    if name not in unique_names:
        unique_names.append(name)

for name in unique_names:

    print(name)