from collections import deque

stack = []

number_of_queriers = int(input())

for _ in range(number_of_queriers):

    command = input().split()

    if len(command) == 2:

        number = int(command[1])

        stack.append(number)

    else:

        digit = int(command[0])

        if digit == 2 and stack:

            stack.pop()

        elif digit == 3 and stack:

            print(max(stack))

        elif digit == 4 and stack:
            print(min(stack))


while stack:
    element = stack.pop()

    if stack:
        print(element, end= ", ")

    else:
        print(element)