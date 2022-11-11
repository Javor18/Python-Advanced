matrix_size = int(input())

matrix = []

for i in range(matrix_size):

    nums = [int(x) for x in input().split()]

    matrix.append(nums)

sum = 0

# for row in range(matrix_size):
#
#     for col in range(matrix_size):
#
#         if row == col:
#
#             sum += matrix[row][col]

for i in range(matrix_size):

    sum += matrix[i][i]

print(sum)