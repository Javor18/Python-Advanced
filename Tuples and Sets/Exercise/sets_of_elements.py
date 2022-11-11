# n, m = map(int, input().split())
#
# first_set = []
# second_set = []
#
# for x in range(n):
#
#     num = input()
#     first_set.append(num)
#
# for y in range(m):
#
#     num = input()
#     second_set.append(num)
#
# for num in first_set:
#
#     if num in second_set:
#
#         print(num)


n, m = map(int, tuple(input().split()))

first_set, second_set = set(), set()

for i in range(n):
    first_set.add(int(input()))

for z in range(m):
    second_set.add((int(input())))

for element in first_set & second_set:

    print(element)