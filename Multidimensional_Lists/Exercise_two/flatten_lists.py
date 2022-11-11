command = input().split("|")

new_string = []

for string in command[::-1]:

    new_string.extend(string.split())

print(" ".join([str(x) for x in new_string]))