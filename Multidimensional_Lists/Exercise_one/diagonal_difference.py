size = int(input())

matrix = []

for i in range(size):

    matrix.append([int(x) for x in input().split()])

primary_diagonal = []

secondary_diagonal = []

for i in range(size):

    primary_diagonal.append(matrix[i][i])

    secondary_diagonal.append(matrix[i][size - i - 1])

primary_sum = sum(primary_diagonal)

secondary_sum = sum(secondary_diagonal)

total_sum = abs(primary_sum - secondary_sum)

print(total_sum)