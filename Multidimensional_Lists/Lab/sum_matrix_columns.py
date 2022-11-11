rows, cols = [int(x) for x in input().split(", ")]

matrix = []

for i in range(rows):

    nums = [int(el) for el in input().split()]

    matrix.append(nums)

for col_index in range(cols):

    sum = 0

    for row_index in range(rows):

        sum += matrix[row_index][col_index]

    print(sum)