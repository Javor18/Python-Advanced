rows, columns = [int(x) for x in input().split()]

string = input()

index = 0

for row in range (rows):

    row_elements = [None] * columns

    if row % 2 == 0:

        for col in range (columns):

            row_elements[col] = string[index % len(string)]

            index += 1

    else:

        for col in range (columns - 1, -1, -1):

            row_elements[col] = string[index % len(string)]
            index += 1

    print(*row_elements, sep= "")